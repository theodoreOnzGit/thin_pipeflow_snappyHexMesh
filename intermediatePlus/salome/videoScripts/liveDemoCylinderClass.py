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
        
    def getFaceGroup(self):

        return self.faceGroup

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


    # this function returns a set of faces from the shape

    def buildGroupFromShape(self,shape = 'cylinder2'):

        if shape == 'cylinder1':
            
            self.faceGroup = self.geompy.CreateGroup(self.buildCylinder1(), self.geompy.ShapeType["FACE"])

        elif shape == 'cylinder2':

            self.faceGroup = self.geompy.CreateGroup(self.buildCylinder2(), self.geompy.ShapeType["FACE"])

        else:

            self.faceGroup = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])

        return self.faceGroup

    def buildFaceListFromShape(self,shape = 'cylinder2'):

        if shape == 'cylinder1':
            shape = self.buildCylinder1()

        elif shape == 'cylinder2':
            shape = self.buildCylinder2()

        self.faceList  = self.geompy.SubShapeAllSortedCentres(shape, self.geompy.ShapeType["FACE"])

        return self.faceList

    def buildBottomInletFace(self,faceList,shape):

        # first, we get our two points, the face and the bottom vertex

        bottomInletVertex = self.getBottomInletPoint() 

        # second, we measure distance

        for face in faceList:

            distance = self.getMinDist(startPoint = bottomInletVertex, endPoint = face)

          

        # third, if distance = 0, then we add that specific face to the group

            if distance == 0:

        # 3(i) we will first get the faceID

        # 3(ii) then we will use the faceID to add the face to the correct shape
                   FaceID = self.geompy.GetSubShapeID(shape, face)

                   inlet = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])
                   self.geompy.UnionIDs(inlet, [FaceID])

                   self.geompy.addToStudyInFather(shape, inlet, 'bottomInlet' )

        self.updateBrowser()


    def buildTopOutletFace(self,faceList,shape):

        # first, we get our two points, the face and the bottom vertex

        topOutletVertex = self.getTopOutletPoint() 

        # second, we measure distance

        for face in faceList:

            distance = self.getMinDist(startPoint = topOutletVertex, endPoint = face)

          

        # third, if distance = 0, then we add that specific face to the group

            if distance == 0:

                   FaceID = self.geompy.GetSubShapeID(shape, face)

                   outlet = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])
                   self.geompy.UnionIDs(outlet, [FaceID])

                   self.geompy.addToStudyInFather(shape, outlet, 'topOutlet' )

        self.updateBrowser()

    def buildCurvedWallFace(self,faceList,shape):

        # first, we get our two points, the face and the bottom vertex

        topOutletVertex = self.getTopOutletPoint() 

        # second, we measure distance

        for face in faceList:

            distance = self.getMinDist(startPoint = topOutletVertex, endPoint = face)

            radius = self.getRadius() 

            difference = distance - radius

        # third, if distance = 0, then we add that specific face to the group

            if difference == 0:

                   FaceID = self.geompy.GetSubShapeID(shape, face)

                   wall = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])
                   self.geompy.UnionIDs(wall, [FaceID])

                   self.geompy.addToStudyInFather(shape, wall , 'curvedWall' )

        self.updateBrowser()



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

        self.printTestDescription()

    
    def printTestDescription(self):

        print(" ")
        print("test description:")
        print(" ")
        print("test.testCylinderObj()")
        print("tests meshing of a cylinder without faces")
        print(" ")

        print(" ")
        print("test.testFaceName()")
        print("tests adding faces to a cylinder")
        print(" ")


        print(" ")
        print("test.testFaceMeshing()")
        print("tests meshing of a cylinder with faces")
        print(" ")


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

        # we are initiating the cylinder build process

        cylinderObj = self.getCylinderObj()
        cylinderObj.buildOrigin()
        cylinder2 = cylinderObj.buildCylinder2()

        # now we need to get the vertices for minimum distance

        topOutletPoint = cylinderObj.getTopOutletPoint()
        bottomInletPoint = cylinderObj.getBottomInletPoint()

        # let's return a group of faces (important for adding objects to geopy)

        faceGroup = cylinderObj.buildGroupFromShape(shape = cylinder2)

        print(faceGroup)

        # let's also return a list of faces so that we can compare distance

        faceList = cylinderObj.buildFaceListFromShape(shape = cylinder2)

        print(faceList)

        for face in faceList:
            print(face)

            distance = cylinderObj.getMinDist(startPoint = bottomInletPoint, endPoint = face)

            print(distance)

        cylinderObj.buildBottomInletFace(faceList = faceList, shape = cylinder2)

        cylinderObj.buildTopOutletFace(faceList = faceList, shape = cylinder2)

        cylinderObj.buildCurvedWallFace(faceList = faceList, shape = cylinder2)


    def testFaceMeshing(self):

        pass


######################################################################################################
######################################################################################################
######################################################################################################

class workspace:

    def __init__(self):


        print('loading workspace')

        self.importModules()

        self.printObjectDeclaration()


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

    def printObjectDeclaration(self):

        print("to get the tests object, type:")
        print(' ')
        print("test = self.getTestObj()")

        print(" ")
        print("to get the cylinder object, type:")
        print("cylinder = self.getCylinderObj()")
        print(" ")











