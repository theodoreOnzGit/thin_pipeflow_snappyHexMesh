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

        self.sys = sys
        self.salome = salome

        self.salome.salome_init()
        self.salome_notebook = salome_notebook

        self.notebook = salome_notebook.NoteBook()

        self.GEOM = GEOM
        self.geomBuilder = geomBuilder
        self.math = math
        self.SALOMEDS = SALOMEDS

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
