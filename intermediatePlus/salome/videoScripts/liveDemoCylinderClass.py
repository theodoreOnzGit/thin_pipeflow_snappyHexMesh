class meshBuilder:

    # constructor function/method

    def __init__(self):

        # let's print the intro

        self.printIntro()

        # first we import modules
        self.importModules()


        # then we initialise salome objects

        self.initialiseSalomeObjects()

        # we need to initialise a geompy object

        self.setGeompy('new')


        # next we give some default dimensions

        self.setDimensionDefaults()



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

        O = self.geompy.MakeVertex(0, 0, 0)
        OX = self.geompy.MakeVectorDXDYDZ(1, 0, 0)
        OY = self.geompy.MakeVectorDXDYDZ(0, 1, 0)
        OZ = self.geompy.MakeVectorDXDYDZ(0, 0, 1)
        self.geompy.addToStudy( O, 'O' )
        self.geompy.addToStudy( OX, 'OX' )
        self.geompy.addToStudy( OY, 'OY' )
        self.geompy.addToStudy( OZ, 'OZ' )

        self.updateBrowser()

        return self.getGeompy()


    def buildCylinder1(self,radius='default',height='default', cylinderName='cylinder1'):


        if radius == 'default':

            radius = self.getRadius()

        if height == 'default':

            height = self.getCylinderHeight()

        cylinder1 = self.geompy.MakeCylinderRH(radius, height)
        self.geompy.addToStudy( cylinder1, cylinderName )

        self.updateBrowser()

        self.cylinder1 = cylinder1

        return self.cylinder1


    def buildCylinder2(self,radius='default', cylinderName='cylinder2'):

        # first we build some dimensions for the cylinder 
        
        if radius == 'default':

            radius = self.getRadius()

        bottomInletPoint = self.getBottomInletPoint()
        topOutletPoint = self.getTopOutletPoint()

        # next, we determine the height of the cylinder        

        height = self.getMinDist(startPoint = bottomInletPoint, endPoint = topOutletPoint)

        # thirdly we get the vector necessary for cylinder construction

        vector = self.getVector(startPoint = bottomInletPoint, endPoint = topOutletPoint)

        cylinder2 = self.geompy.MakeCylinder(bottomInletPoint, vector, radius, height)
        self.geompy.addToStudy( cylinder2, cylinderName )

        self.updateBrowser()

        self.cylinder2 = cylinder2

        return self.cylinder2



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
        elif geompy == 'new':
            self.geompy = self.geomBuilder.New()
        else:
            self.geompy = geompy


    def setRadius(self,radius=100):

        self.radius=radius

    def getRadius(self):

        return self.radius

    def setCylinderHeight(self,height=300):

        self.cylinderHeight = height

    def getCylinderHeight(self):

        return self.cylinderHeight

    def setBottomInletPoint(self,point=(0,0,-150)):

        x = point[0]
        y = point[1]
        z = point[2]

        self.bottomInletPoint = self.geompy.MakeVertex(x,y,z)

    def getBottomInletPoint(self):

        return self.bottomInletPoint



    def setTopOutletPoint(self,point=(0,0,150)):

        x = point[0]
        y = point[1]
        z = point[2]

        self.topOutletPoint = self.geompy.MakeVertex(x,y,z)

    def getTopOutletPoint(self):

        return self.topOutletPoint
        

    def setDimensionDefaults(self):

        self.setTopOutletPoint()
        self.setBottomInletPoint()
        self.setCylinderHeight()
        self.setRadius()

######################################################################################################

# this section does intermeditate calculations

    def getMinDist(self,startPoint,endPoint):

        return self.geompy.MinDistance(startPoint, endPoint)

    def getVector(self,startPoint,endPoint):

        return self.geompy.MakeVector(startPoint,endPoint)





######################################################################################################
######################################################################################################
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
        cylinder1 = cylinderObj.buildCylinder1()
        mesh1 = cylinderObj.meshShapeNETGEN1D2D3D(cylinder1)


    def testFaceName(self):

        cylinderObj = self.getCylinderObj()
        cylinderObj.buildOrigin()
        cylinder2 = cylinderObj.buildCylinder2()






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

    def printHelp(self):

        print(' ')
        print('This is the printHelp function')
        print('to get the test object, use getTestObj()')
        print('to get the cylinder object, use getCylinderObj()')
        print(' ')












