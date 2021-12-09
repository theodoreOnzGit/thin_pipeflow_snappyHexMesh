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

    def setBottomInletPoint(self,point='default'):

        # this function takes in a tuple as its argument

        if point == 'default':
            point = (0,0,-150)

        else:
            pass

        pointX = point[0]
        pointY = point[1]
        pointZ = point[2]

        self.bottomInletPoint = self.geompy.MakeVertex(pointX,pointY,pointZ)
    
        return self.bottomInletPoint


    def setTopOutletPoint(self,point='default'):

        # this function takes in a tuple as its argument

        if point == 'default':
            point = (0,0,150)

        else:
            pass

        pointX = point[0]
        pointY = point[1]
        pointZ = point[2]

        self.topOutletPoint = self.geompy.MakeVertex(pointX,pointY,pointZ)







    def getCylinderRadius(self):

        return self.cylinderRadius

    def getCylinderHeight(self):

        return self.cylinderHeight

    def getCylinder1(self):

        return self.cylinder1

    def getCylinder2(self):

        return self.cylinder2


    def getTopOutletPoint(self):

        return self.topOutletPoint

    def getBottomInletPoint(self):

        return self.bottomInletPoint


# the following section sets some defaults

    def setDefaults(self):

        self.buildOrigin()
        self.setCylinderRadius()
        self.setCylinderHeight()
        self.setTopOutletPoint()
        self.setBottomInletPoint()





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

        print('if you want to build a cylinder specifying radius, and bottom and top points, use:')
        print('buildCylinder2')

        print(' ')

        print('To check the values of cylinder height and radius you can try')

        print('objectName.getCylinderHeight(), and objectName.getCylinderRadius()')

        print('To check values of a cylinder bottom and top point, you can try:')
        print('objectName.getBottomInletPoint() and objectName.getTopOutletPoint')

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

    def meshAddParameters(self,compute=True):

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

        if compute == True:
            self.meshCompute()




    def meshCompute(self):
        isDone = self.mesh1.Compute()
        self.smesh.SetName(self.NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')


    def meshAddInlet(self):

        self.mesh1.GroupOnGeom(self.getInletFace(),self.getInletName(),self.SMESH.FACE)

    def meshAddOutlet(self):

        self.mesh1.GroupOnGeom(self.getOutletFace(),self.getOutletName(),self.SMESH.FACE)

    def meshAddWall(self):

        self.mesh1.GroupOnGeom(self.getWallFace(),self.getWallName(),self.SMESH.FACE)



#######################################################################################################################


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


    def helloThere(self):

        print('hello there')

    def getGroupFaceListFromShape(self,shape='default'):

        if shape == 'default':
            
            self.group = self.geompy.CreateGroup(self.getCylinder1(), self.geompy.ShapeType["FACE"])
            self.faceList = self.geompy.SubShapeAllSortedCentres(self.getCylinder1(), self.geompy.ShapeType["FACE"])
        else:
            self.group = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])
            self.faceList = self.geompy.SubShapeAllSortedCentres(shape, self.geompy.ShapeType["FACE"])


        return self.faceList

    def getGroupFromShape(self,shape = 'default'):

        if shape == 'default':
            
            self.group = self.geompy.CreateGroup(self.getCylinder1(), self.geompy.ShapeType["FACE"])
        else:
            self.group = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])


        return self.group

    def getFaceIDListFromShape(self,shape = 'cylinder2'):

        if shape == 'default':
            shape = self.getCylinder1()

        elif shape == 'cylinder2':
            shape = self.getCylinder2()

        faceList  = self.getGroupFaceListFromShape(shape = shape)

        faceIDList = []

        for i in range(len(faceList)):

            FaceID = self.geompy.GetSubShapeID(shape, faceList[i])
            faceIDList.append(FaceID)


        return faceIDList

#######################################################################################################

# these are functions that deal specifically with one face object, identify it and add it


    def addInletToCylinder(self,face,shape = 'cylinder2'):

        if shape == 'cylinder2':

            shape = self.getCylinder2()

        # suppose i have the face, i can get the id straightaway

        faceID = self.geompy.GetSubShapeID(shape,face)

        # i can also measure distance between this face an a set point

        # in this case the point is the inlet

        inletPoint = self.getBottomInletPoint()

        # next thing is to measure distance between the inlet point and the face

        minDistance = self.getMinimumDistance(inletPoint,face)

        # so by default if the minimum distance is 0 (exactly), then i know its the inlet point
        # if i know so, then i can add the inlet straightaway 
        
        if minDistance == 0:

            inlet = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])
            self.geompy.UnionIDs(inlet, [faceID])
            self.geompy.addToStudyInFather(shape, inlet, 'inlet' )
            self.update()

            self.setInletFace(inlet)
            self.setInletName('inlet')


    def setInletFace(self,inlet):

        self.inlet = inlet

    def getInletFace(self):

        return self.inlet

    def setInletName(self,inletName='inlet'):

        self.inletName = inletName

    def getInletName(self):

        return self.inletName



    def addOutletToCylinder(self,face,shape = 'cylinder2'):

        if shape == 'cylinder2':

            shape = self.getCylinder2()

        # suppose i have the face, i can get the id straightaway

        faceID = self.geompy.GetSubShapeID(shape,face)

        # i can also measure distance between this face an a set point

        # in this case the point is the outlet

        outletPoint = self.getTopOutletPoint()

        # next thing is to measure distance between the outlet point and the face

        minDistance = self.getMinimumDistance(outletPoint,face)

        # so by default if the minimum distance is 0 (exactly), then i know its the outlet point and outlet face
        # if i know so, then i can add the outlet straightaway 
        
        if minDistance == 0:

            outlet = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])
            self.geompy.UnionIDs(outlet, [faceID])
            self.geompy.addToStudyInFather(shape, outlet, 'outlet' )
            self.update()

            self.setOutletFace(outlet)
            self.setOutletName('outlet')

    def setOutletFace(self,outlet):

        self.outlet = outlet

    def getOutletFace(self):

        return self.outlet

    def setOutletName(self,outletName='outlet'):

        self.outletName = outletName

    def getOutletName(self):

        return self.outletName




    def addWallToCylinder(self,face,shape = 'cylinder2'):

        if shape == 'cylinder2':

            shape = self.getCylinder2()

        # suppose i have the face, i can get the id straightaway

        faceID = self.geompy.GetSubShapeID(shape,face)

        # i can also measure distance between this face an a set point

        # in this case the point is the inlet

        inletPoint = self.getBottomInletPoint()

        # next thing is to measure distance between the inlet point and the face

        minDistance = self.getMinimumDistance(inletPoint,face)

        # so by default if the minimum distance is the cylinder radius (exactly), then i know the shape is the wall
        # if i know so, then i can add the wall straightaway 
       
        difference = minDistance - self.getCylinderRadius()  

        # if the difference between the minimum distance and cylinder radius is zero, then
        # i can add the wall straight away


        if difference == 0:

            wall = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])
            self.geompy.UnionIDs(wall, [faceID])
            self.geompy.addToStudyInFather(shape, wall, 'wall' )
            self.update()

            self.setWallFace(wall)
            self.setWallName('wall')



    def setWallFace(self,wall):

        self.wall = wall

    def getWallFace(self):

        return self.wall

    def setWallName(self,wallName='wall'):

        self.wallName = wallName

    def getWallName(self):

        return self.wallName







########################################################################################################

### here are functions to probe the shape geometry

# this following function returns a list of normal vectors from a list of faces

    def returnFaceNormalVectors(self, faceList):

        normalList = []

        for face in faceList:

            normalVector = self.geompy.GetNormal(face)

            normalList.append(normalVector)

        return normalList


    def printMinimumDistance(self,obj1,obj2):

        minDistance = self.geompy.MinDistance(obj1,obj2)

        print('the minimum distance between object 1 and object 2 is:', minDistance)



    def getMinimumDistance(self,obj1,obj2):

        minDistance = self.geompy.MinDistance(obj1,obj2)

        return minDistance

    def getMinimumDistanceVector(self,obj1,obj2):


        # the vector to be returned is a tuple


        [aDist, DX, DY, DZ] = self.geompy.MinDistanceComponents(obj1,obj2)

        # the vector will be calculated as coordiantes of obj1 minus coordinates of obj2

        vector = (DX,DY,DZ)

        return vector

#########################################################################################################

# here is buildCylinder2, i might move it elsewhere for neatness sake


    def buildCylinder2(self):


        # firstly, i'll load in all the coordinates

        topOutletPoint = self.getTopOutletPoint()
        bottomInletPoint = self.getBottomInletPoint()
        cylinderRadius = self.getCylinderRadius()
        
        # secondly, i'll build the derived quantities, eg.vector1, height and etc

        # the two points to specify in this vector by position is the start point, then the end poin
                # the two points to specify in this vector by position is the start point, then the end pointt
        vector1 =  self.geompy.MakeVector(bottomInletPoint,topOutletPoint)

        height = self.getMinimumDistance(bottomInletPoint,topOutletPoint)


        self.cylinder2 = self.geompy.MakeCylinder(bottomInletPoint, vector1, cylinderRadius, height)

        self.geompy.addToStudy( self.cylinder2 , 'cylinder2')

        self.update()

        return self.cylinder2


########################################################################################################

# here are functions to clear the workspace

    def clearOrigin(self):


        # still buggy, just a placeholder method/function

        #self.geompy.RemoveObject('OX')
        #self.geompy.RemoveObject('OY')
        #self.geompy.RemoveObject('OZ')



        #self.update()
        pass


    def clearShape(self,shape):

        # this function uses the geomtools class
        # https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__geomtools.html

        from salome.geom.geomtools import GeomStudyTools
        geomStudyObj = GeomStudyTools()
        GeomStudyTools.deleteShape(shape)

        # still needs debug, reference here for class definitions

        # https://github.com/FedoraScientific/salome-gui/blob/master/src/SalomeApp/pluginsdemo/xalome.py
        


    def clearAll(self):

        # this section of code is meant to clear everything, but is not functioning now

        # https://www.salome-platform.org/forum/forum_10/740853490

        for compName in ["SMESH","GEOM"]:

            comp = self.salome.myStudy.FindComponent(compName)

            if comp:

                iterator = self.salome.myStudy.NewChildIterator( comp )
                while iterator.More():
                    sobj = iterator.Value()
                    iterator.Next()
                    nb.RemoveObjectWithChildren( sobj )

########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
########################################################################################################
class tests:


    def __init__(self):

        from cylinderClass import cylinderMesh
        self.cylinderMesh = cylinderMesh

        self.printTestDescription()


    def printTestDescription(self):

        print(" ")
        print("welcome to the tests object")
        print("here we run specific tests for the cylinder object")
        
        print(" ")
        print("test.test1()")
        print("does basic meshing and shape addition without faces")
        print(" ")

        print(" ")
        print("test.test2()")
        print("gets group face lists from particular shapes")
        print(" ")

        print(" ")
        print("test.faceListTest()")
        print("investigates how to deal with faces in salome")
        print(" ")

        print(" ")
        print("test.faceNamingTest()")
        print("investigates how to name faces and add them to the desired shape")
        print(" ")

        print(" ")
        print("test.faceMeshingTest()")
        print("investigates how to mesh with named faces")
        print(" ")

        print(" ")
        print("test.test4()")
        print("investigates writing input and output files")
        print(" ")


    def test1(self):

        self.cylinderObj = self.getCylinderObj()
        self.cylinderObj.buildOrigin()
        self.cylinderObj.buildCylinder1()
        self.cylinderObj.meshInit()
        self.cylinderObj.meshAddShape()
        self.cylinderObj.meshAddAlgorithmNetgen1D2D3D()
        self.cylinderObj.meshAddParameters()

        self.cylinderObj.unvExport()
        self.cylinderObj.update()

    def test2(self):

        self.cylinderObj = self.getCylinderObj()
        self.cylinderObj.buildOrigin()

        self.cylinderObj.buildCylinder1()
        
        faceList  = self.cylinderObj.getGroupFaceListFromShape()

        print(faceList)

        for i in faceList:

            print(i)

        print("length of face list is: ",len(faceList))

        faceIDList = []

        for i in range(len(faceList)):

            FaceID = self.cylinderObj.geompy.GetSubShapeID(self.cylinderObj.getCylinder1(), faceList[i])

            print(FaceID)
            faceIDList.append(FaceID)

        print(faceIDList)

        # now we can see the faceIDList, and we can get all the faceIDs, great!

        # next is how can we visualise the faceIDs??

        # https://docs.salome-platform.org/latest/gui/GEOM/tui_working_with_groups_page.html

        # in the above doc, the group object has the faces

        # and the faceID is used to get individual face objects...
        # we don't see any way of interfacing with these objects. I suppose one 
        # has to do the naming convention manually

        # because it is hard to visualise in code space what these faces are like

        # we can still get length breadth and etc

        # https://www.salome-platform.org/forum/forum_14/550791677

        # https://www.salome-platform.org/forum/forum_10/638257047#206420738

        # one way is to get the normals of the surfaces, a python dump file already shows how to get that
        # the other way is to get the properties of the surface
        # yet another way of differentiating surfaces is their position relative to a point

        # this is done using the minimum distance code outlined here:
        # https://docs.salome-platform.org/7/gui/GEOM/min_distance_page.html

        # other object properties can be probed here:
        # https://docs.salome-platform.org/7/gui/GEOM/using_measurement_tools_page.html

        # in each of these documentation pages, you can find what you need, eg. center of mass, inertia, etc.


        print('test 2 complete')

        return faceList

    def faceListTest(self):

        # this first part of the test prints normals associated with the face list

        self.cylinderObj = self.getCylinderObj()

        self.cylinderObj.buildCylinder1()
        
        faceList  = self.cylinderObj.getGroupFaceListFromShape()

        normalVectorList = self.cylinderObj.returnFaceNormalVectors(faceList)

        for vector in normalVectorList:

            print(vector)
            Descr = self.cylinderObj.geompy.WhatIs(vector)
            print(Descr)

        print('face list normal test complete')

        # note that vectors are objects, and cannot be printed straightaway

        # so they may not be so useful at the moment

        # the second part i want to try is the minimum distance from a point


        originPoint = self.cylinderObj.geompy.MakeVertex(0,0,0)

        totalDistance = 0

        for face in faceList:

            self.cylinderObj.printMinimumDistance(face,originPoint)
        
            # to use getMinimumDistanceVector, you must present the positional arguments
            # initial point, and then final point
            minDistanceVector = self.cylinderObj.getMinimumDistanceVector(originPoint,face) 

            totalDistance += self.cylinderObj.getMinimumDistance(face,originPoint) 

            print('the minimum distance vector is:',minDistanceVector)

        print('total minimum distance is: ',totalDistance)

        print('face minimum distance test complete')


        # if we know where the face should be in coordinate space, then we can use that to locate and automatically name the
        # faces in each cylinder!

        # next thing is to start naming the faces by their coordinates!

        # how do i do this?

    
    def faceNamingTest(self):

        # this test is meant to automate the creation of a cylinder and the process of naming the faces
        # of said cylinder

        self.cylinderObj = self.getCylinderObj()

        # now, i want to make a cylinder with a set radius, height, and two fixed points or vertices
        # the bottom vertex will form the base of the plate

        # so let's build cylinder class 2 first


        # the bottom point i may call the inlet point and the top point i may call the outlet point
        # i will call it bottomInletPoint, and topOutletPoint respectively

        # the vector constructed will be using the top and bottom points

        # thus the cylinder will be constructed. I will then make groups 

        cylinder2 = self.cylinderObj.buildCylinder2()


        # to create faces, we need to first create a group

        # for example, in the python dump file, we see:

        # inlet = geompy.CreateGroup(Cylinder_1, geompy.ShapeType["FACE"])
        # geompy.UnionIDs(inlet, [3])
        # geompy.addToStudyInFather( Cylinder_1, inlet, 'inlet' )

        # here the inlet group is created, it assigns the face number 3 to inlet using the unionID function
        # then adds it to cylinder_1 as a add to studyInFather kind of class

        # now how did we get number [3]? we needed to get a faceList first

        faceIDList = self.cylinderObj.getFaceIDListFromShape(shape=cylinder2)

        print(faceIDList)

        faceList = self.cylinderObj.getGroupFaceListFromShape(shape=cylinder2)

        # from a face list, i can get the faceID and the face object for distance measurement!
        # once i measure the distance and get the id of that face, i can start identifying and naming the face
        
        for face in faceList:

            self.cylinderObj.addInletToCylinder(face,shape=cylinder2)
            self.cylinderObj.addOutletToCylinder(face,shape=cylinder2)
            self.cylinderObj.addWallToCylinder(face,shape=cylinder2)


        print('face adding tests complete!')

    def faceMeshingTest(self):

        # this test is meant to automate the creation of a cylinder and the process of naming the faces
        # of said cylinder plus meshing
        # the first few steps are pretty much the same as the faceNamingTest

        self.cylinderObj = self.getCylinderObj()
        cylinder2 = self.cylinderObj.buildCylinder2()
        faceIDList = self.cylinderObj.getFaceIDListFromShape(shape=cylinder2)
        faceList = self.cylinderObj.getGroupFaceListFromShape(shape=cylinder2)
        
        for face in faceList:

            self.cylinderObj.addInletToCylinder(face,shape=cylinder2)
            self.cylinderObj.addOutletToCylinder(face,shape=cylinder2)
            self.cylinderObj.addWallToCylinder(face,shape=cylinder2)


        print('face adding complete!')

        # now with the face adding complete, i will need to start a meshing process

        # the first few steps are usually the following:

        #(1) we intiate an smesh object using meshInit()
        
        self.cylinderObj.meshInit()

        #(2) we add the shape to the mesh, in this case cylinder2
        self.cylinderObj.meshAddShape(shape=cylinder2)
        # the name of the mesh object is mesh1

        #(3) according to the python dump file, we can add the algorithm and mesh parameters next
        self.cylinderObj.meshAddAlgorithmNetgen1D2D3D()
        self.cylinderObj.meshAddParameters(compute=False)

        #(4) next is quite important, we need to add faces to the mesh

        self.cylinderObj.meshAddInlet()
        self.cylinderObj.meshAddOutlet()
        self.cylinderObj.meshAddWall()

        #(5) lastly we'll compute

        self.cylinderObj.meshCompute()

        #(6 & 7) lastly we export to unv and update
        self.cylinderObj.unvExport()
        self.cylinderObj.update()

    def test4(self):

        # this is an input output writer test

        foamWriterObj = self.getFoamWriterObj()

        foamWriterObj.overwriteTest1()

        for i in range(7):
            foamWriterObj.appendTest2()


        # now i'm able to write input and output files as and how i like for openfoam!
        












    def comments(self):

        

        # last but not least (not related to this python script), it is interesting to see 
        # some good shortcuts, eg ctrl-r
        # and also configuring github to automatically fill in password everytime during a push

        # this is best done using ssh
        # https://stackoverflow.com/questions/8588768/how-do-i-avoid-the-specification-of-the-username-and-password-at-every-git-push

        pass


    def getCylinderObj(self):

        self.cylinderObj = self.cylinderMesh()

        return self.cylinderObj

    def getFoamWriterObj(self):

        import inputOutputWriter

        inputOutputWriter = self.reload(inputOutputWriter)

        from inputOutputWriter import foamWriter

        foamWriterObj = foamWriter()

        return foamWriterObj


    def reload(self,pythonFile):

        from importlib import reload
        reload(pythonFile)

        return pythonFile

class workspace:

    def __init__(self):

        print('initialising workspace...')

        self.initialiseDefaults()

        self.printObjectDeclaration()

        
    def printObjectDeclaration(self):

        print("to get the tests object, type:")
        print(' ')
        print("test = self.getTestsObj()")

        print(" ")
        print("to get the cylinder object, type:")
        print("cylinder = self.getCylinderObj")


    def getTestsObj(self):

        self.reloadClasses()
        self.testsObj = self.tests()

        return self.testsObj


    def getCylinderObj(self):

        self.reloadClasses()
        self.cylinderObj = self.cylinderMesh()

        return self.cylinderObj

    def initialiseDefaults(self):

        import cylinderClass
        from cylinderClass import cylinderMesh

        from cylinderClass import tests

        self.cylinderClass = cylinderClass
        self.cylinderMesh = cylinderMesh
        self.tests = tests


        from importlib import reload

        self.reload = reload


    def reloadClasses(self):

        # this bit reloads the cylinder class

        reload = self.reload
        import cylinderClass
        reload(cylinderClass)
        from cylinderClass import cylinderMesh

        self.cylinderClass = cylinderClass
        self.cylinderMesh = cylinderMesh

        # we also re-import loaded tests

        from cylinderClass import tests

        self.tests = tests


        # now we also import a new inputOutputWriter object

        import inputOutputWriter
        reload(inputOutputWriter)

        self.inputOutputWriter = inputOutputWriter


    def getFoamWriterObj(self):

        self.reloadClasses()

        from inputOutputWriter import foamWriter

        foamWriterObj = foamWriter()

        return foamWriterObj
