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

        return self.getGeompy()


    def buildCylinder(self,radius=100,height=300, cylinderName='cylinder1'):

        geompy = self.getGeompy()

        cylinder1 = geompy.MakeCylinderRH(radius, height)
        geompy.addToStudy( cylinder1, cylinderName )


        self.setGeompy(geompy)

        return self.getGeompy()




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


    def reloadModules(self):

        reload = self.reload

        import liveDemoCylinderClass
        reload(liveDemoCylinderClass)

        self.liveDemoCylinderClass = liveDemoCylinderClass

        # import the meshbuilder class
        from liveDemoCylinderClass import meshBuilder
        self.meshBuilder = meshBuilder


    def getCylinderObj(self):

        self.reloadModules()
        cylinderObj = self.meshBuilder()

        return cylinderObj














