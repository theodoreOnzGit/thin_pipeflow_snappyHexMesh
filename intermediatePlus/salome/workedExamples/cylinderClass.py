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

    def getCylinder1(self):

        return self.cylinder1


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


    def helloThere(self):

        print('hello there')

    def getGroupFaceListFromShape(self,shape='default'):

        if shape == 'default':
            
            self.group = self.geompy.CreateGroup(self.getCylinder1(), self.geompy.ShapeType["FACE"])
            self.subFaceList = self.geompy.SubShapeAllSortedCentres(self.getCylinder1(), self.geompy.ShapeType["FACE"])
        else:
            self.group = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])
            self.subFaceList = self.geompy.SubShapeAllSortedCentres(shape, self.geompy.ShapeType["FACE"])


        return self.subFaceList

    def getGroupFromShape(self,shape = 'default'):

        if shape == 'default':
            
            self.group = self.geompy.CreateGroup(self.getCylinder1(), self.geompy.ShapeType["FACE"])
        else:
            self.group = self.geompy.CreateGroup(shape, self.geompy.ShapeType["FACE"])


        return self.group

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


    def getCylinderObj(self):

        self.cylinderObj = self.cylinderMesh()

        return self.cylinderObj


class workspace:

    def __init__(self):

        print('initialising workspace...')

        self.initialiseDefaults()


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
