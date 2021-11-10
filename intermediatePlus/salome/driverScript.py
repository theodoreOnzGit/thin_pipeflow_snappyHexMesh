## this script helps to initiate an object to use the salome scripts

from salomeScriptClass import meshAutomator
meshAutomatorObj = meshAutomator()

def reloadClasses():

    # this bit reloads the cylinder class

    from importlib import reload
    import cylinderClass
    reload(cylinderClass)
    from cylinderClass import cylinderMesh
    cylinderObj = cylinderMesh()


reloadClasses()

