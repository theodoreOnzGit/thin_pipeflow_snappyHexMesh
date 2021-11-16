class meshBuilder:

    # constructor function/method

    def __init__(self):

        # let's print the intro

        self.printIntro()

        # first we import modules
        self.importModules()


        # then we initialise salome objects

        self.initialiseSalomeObjects()


    # initialise salome notebook and mesh

    def initialiseSalomeObjects(self):

        self.salome.salome_init()
        self.notebook = self.salome_notebook.NoteBook()
        self.smesh = self.smeshBuilder.New()




    # import important modules
       
    def importModules(self):

        import sys
        import salome
        import salome_notebook

        ###
        ### GEOM component
        ###

        import GEOM
        from salome.geom import geomBuilder
        import math

        ###
        ### SMESH component
        ###

        import  SMESH, SALOMEDS
        from salome.smesh import smeshBuilder

        ### load modules into the object instance

        self.sys = sys
        self.salome = salome
        self.salome_notebook = salome_notebook

        self.GEOM = GEOM
        self.geomBuilder = geomBuilder
        self.math = math
        self.SALOMEDS  = SALOMEDS

        self.SMESH = SMESH
        self.smeshBuilder = smeshBuilder

    def buildOrigin(self):

        geompy = self.geomBuilder.New()

        O = geompy.MakeVertex(0, 0, 0)
        OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
        OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
        OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
        geompy.addToStudy( O, 'O' )
        geompy.addToStudy( OX, 'OX' )
        geompy.addToStudy( OY, 'OY' )
        geompy.addToStudy( OZ, 'OZ' )

        self.setGeompy(geompy)

        self.updateBrowser()

        return self.getGeompy()


    def buildCylinder(self,radius=100,height=300, cylinderName='cylinder1'):

        geompy = self.getGeompy()

        cylinder1 = geompy.MakeCylinderRH(radius, height)
        geompy.addToStudy( cylinder1, cylinderName )


        self.setGeompy(geompy)

        self.updateBrowser()

        self.cylinder1 = cylinder1

        return self.cylinder1


    def updateBrowser(self):

        # this is a function to update the browser
        if self.salome.sg.hasDesktop():
            self.salome.sg.updateObjBrowser()


    def meshShapeNETGEN1D2D3D(self,shape,meshName='mesh1'):

        mesh1 = self.smesh.Mesh(shape)
        NETGEN_1D_2D_3D = mesh1.Tetrahedron(algo=self.smeshBuilder.NETGEN_1D2D3D)
        isDone = mesh1.Compute()

        self.smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
        self.smesh.SetName(mesh1.GetMesh(), meshName)

        self.updateBrowser()

        return mesh1



#####################################################################################################

### here are get and set functions

    def getGeompy(self):

        return self.geompy


    def setGeompy(self,geompy='default'):

        if geompy == 'default':
            pass
        else:
            self.geompy = geompy


        

######################################################################################################

# this section contains code for printing

    def printIntro(self):

        print(' =====================================================')
        print(' ')
        print('cylinder object mesh builder class initiated')
        print(' ')
        print(' =====================================================')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')



######################################################################################################
######################################################################################################
######################################################################################################

class test:

    def __init__(self):


        # firstly import modules in the constructor

        self.importModules()




    def importModules(self):

        # importing the reload function
        from importlib import reload
        self.reload = reload

        # importing the liveDemoCylinderClass python module(?)
        import liveDemoCylinderClass
        self.liveDemoCylinderClass = liveDemoCylinderClass

        # import the meshbuilder class
        from liveDemoCylinderClass import meshBuilder
        self.meshBuilder = meshBuilder



    def getCylinderObj(self):

        cylinderObj = self.meshBuilder()
        return cylinderObj


    def testCylinderObj(self):

        # this demonstrates basic functionality for the cylinder object

        cylinderObj = self.getCylinderObj()
        cylinderObj.buildOrigin()
        cylinder1 = cylinderObj.buildCylinder()
        mesh1 = cylinderObj.meshShapeNETGEN1D2D3D(cylinder1)








######################################################################################################
######################################################################################################
######################################################################################################

class workspace:

    def __init__(self):


        print('loading workspace')

        self.importModules()


    def importModules(self):

        # importing the reload function
        from importlib import reload
        self.reload = reload

        # importing the liveDemoCylinderClass python module(?)
        import liveDemoCylinderClass
        self.liveDemoCylinderClass = liveDemoCylinderClass

        # import the meshbuilder class
        from liveDemoCylinderClass import meshBuilder
        self.meshBuilder = meshBuilder

        # import the test class

        from liveDemoCylinderClass import test
        self.test = test

    def reloadModules(self):

        reload = self.reload

        import liveDemoCylinderClass
        reload(liveDemoCylinderClass)

        self.liveDemoCylinderClass = liveDemoCylinderClass

        # import the meshbuilder class
        from liveDemoCylinderClass import meshBuilder
        self.meshBuilder = meshBuilder

        # import the test class

        from liveDemoCylinderClass import test
        self.test = test

    def getCylinderObj(self):

        self.reloadModules()
        cylinderObj = self.meshBuilder()

        return cylinderObj

    def getTestObj(self):

        self.reloadModules()
        testObj = self.test()

        return testObj














