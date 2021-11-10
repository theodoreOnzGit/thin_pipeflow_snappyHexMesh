to use this file, you need to tell salome through the python module to add a folder to the os path

so that you can start initiating objects and letting the code know what to do


to do so, you need to git clone your git directory into the salome directory and import the 

linkGitWorkDirectory.py

into the salome python console.
This will make this folder accessible to all the salome python workspace


note: to re-import modules

we use:
https://stackoverflow.com/questions/6946376/how-to-reload-a-class-in-python-shell

eg. 

import cylinderClass
from cylinderClass import cylinderMesh
cylinderObj = cylinderMesh()

now you made some changes to the class and want to reload it, use:

from importlib import reload
import cylinderClass
reload(cylinderClass)
from cylinderClass import cylinderMesh
cylinderObj = cylinderMesh()

