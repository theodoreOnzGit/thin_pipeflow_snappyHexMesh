# this class will work everything out

# to use this class, you'll need to type in your salome console

# import linkGitWorkDirectory
# from cylinderClass import cylinderMesh
# cylinderMeshObj = cylinderMesh() 

class cylinderMesh:

# this is the constructor

# you have to run this in the salome python console

    def __init__(self):

        # first i want to import the modules

        self.importModules()
        self.setDefaults()
        self.printIntro()
        self.meshInit()

#  this part imports modules for the mesh and geometry


    def importModules(self):

        import sys
        import salome

        import salome_notebook

        ### GEOM component
        ###

        import GEOM
        from salome.geom import geomBuilder
        import math
        import SALOMEDS

        ###     
        ### SMESH component
        ###
        
        import  SMESH
        from salome.smesh import smeshBuilder

        import os

        self.sys = sys
        self.salome = salome

        self.salome.salome_init()
        self.salome_notebook = salome_notebook

        self.notebook = salome_notebook.NoteBook()

        self.GEOM = GEOM
        self.geomBuilder = geomBuilder
        self.math = math
        self.SALOMEDS = SALOMEDS

        self.SMESH = SMESH
        self.smeshBuilder = smeshBuilder
        self.os = os

        print("module import complete")

# this function enables building of the origin based on assuming the origin is (0,0,0)

    def buildOrigin(self):

        self.geompy = self.geomBuilder.New()

        O = self.geompy.MakeVertex(0, 0, 0)
        OX = self.geompy.MakeVectorDXDYDZ(1, 0, 0)
        OY = self.geompy.MakeVectorDXDYDZ(0, 1, 0)
        OZ = self.geompy.MakeVectorDXDYDZ(0, 0, 1)

        self.geompy.addToStudy( OX, 'OX' )
        self.geompy.addToStudy( OY, 'OY' )
        self.geompy.addToStudy( OZ, 'OZ' )

    def buildCylinder1(self):

        self.cylinder1 = self.geompy.MakeCylinderRH(self.getCylinderRadius(),self.getCylinderHeight())

        self.geompy.addToStudy( self.cylinder1 , 'cylinder1')

        print(' ')

        print('cylinder1 built and added to study at height:'+str(self.getCylinderHeight()))
        print('and radius:'+str(self.getCylinderRadius()))

        print(' ' )


# the following section has functions for getting and setting cylinders

    def setCylinderRadius(self,radius=100):

        self.cylinderRadius = radius

        print(r'cylinder radius set at '+str(radius))

    def setCylinderHeight(self,height=300):

        self.cylinderHeight = height

        print(r'cylinder height set at '+str(height))


    def getCylinderRadius(self):

        return self.cylinderRadius

    def getCylinderHeight(self):

        return self.cylinderHeight

# the following section sets some defaults

    def setDefaults(self):

        self.setCylinderRadius()
        self.setCylinderHeight()
        self.buildOrigin()





# the following just prints help and intro

    def printIntro(self):


        print(' ')
        print(' ')
        print('welcome to the cylinder buildMesh class, where we just build a tetrahedral mesh of a cylinder')
        print('for an example')

        print(' ')
        print('use printHelp() to get a sense of how to use the object')

        print(' ')



    def printHelp(self):

        print(' ')
        print('Welcome to the print help interface')

        print('to set the cylinder radius to 250 and height to 300 use:')

        print('objectName.setCylinderRadius(250) and objectName.setCylinderHeight(300)')

        print(' ')

        print('Then if you want to build a new cylinder use')
        print('objectName.buildCylinder1()')

        print(' ')

        print('To check the values of cylinder height and radius you can try')

        print('objectName.getCylinderHeight(), and objectName.getCylinderRadius()')


    def checkShape(self,shape='default'):

        if shape == 'default':
            print(self.geompy.BasicProperties(self.cylinder1))
        else:
            print(self.geompy.BasicProperties(shape))


# now next thing is to build meshes

    def meshInit(self):

        self.smesh = self.smeshBuilder.New()



    def meshAddShape(self,shape='default'):

        if shape == 'default':

            self.mesh1 = self.smesh.Mesh(self.cylinder1)

        else:
            self.mesh1 = self.smesh.Mesh(shape)

        self.smesh.SetName(self.mesh1.GetMesh(),'mesh1')



    def meshAddAlgorithmNetgen1D2D3D(self):

        self.NETGEN_1D_2D_3D = self.mesh1.Tetrahedron(algo=self.smeshBuilder.NETGEN_1D2D3D)
        self.smesh.SetName(self.NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')

    def meshAddParameters(self):

        self.NETGEN_3D_Parameters_1 = self.NETGEN_1D_2D_3D.Parameters()
        self.NETGEN_3D_Parameters_1.SetMaxSize( 41.2311 )
        self.NETGEN_3D_Parameters_1.SetMinSize( 17.4311 )
        self.NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
        self.NETGEN_3D_Parameters_1.SetOptimize( 1 )
        self.NETGEN_3D_Parameters_1.SetFineness( 4 )
        self.NETGEN_3D_Parameters_1.SetChordalError( -1 )
        self.NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 0 )
        self.NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
        self.NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
        self.NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
        self.NETGEN_3D_Parameters_1.SetCheckChartBoundary( 3 )
        isDone = self.mesh1.Compute()
        self.smesh.SetName(self.NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')



    def update(self):

        if self.salome.sg.hasDesktop():
            self.salome.sg.updateObjBrowser()


    def unvExport(self):

        salomeDir = self.os.getcwd()

        fileName = '/mesh1.unv'

        print('attempting unv export at:')
        print(salomeDir+fileName)

        try:
            self.mesh1.ExportUNV( salomeDir+fileName )
            pass
        except:
            print('ExportUNV() failed. Invalid file name?')


class tests:


    def __init__(self):

        from cylinderClass import cylinderMesh
        self.cylinderObj = cylinderMesh()


    def test1(self):

        self.cylinderObj.buildOrigin()
        self.cylinderObj.buildCylinder1()
        self.cylinderObj.meshInit()
        self.cylinderObj.meshAddShape()
        self.cylinderObj.meshAddAlgorithmNetgen1D2D3D()
        self.cylinderObj.meshAddParameters()

        self.cylinderObj.unvExport()
        self.cylinderObj.update()
