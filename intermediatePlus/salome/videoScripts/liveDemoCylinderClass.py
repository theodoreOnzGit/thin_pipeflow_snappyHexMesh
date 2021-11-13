class meshBuilder:

    # constructor function/method

    def __init__(self):



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






