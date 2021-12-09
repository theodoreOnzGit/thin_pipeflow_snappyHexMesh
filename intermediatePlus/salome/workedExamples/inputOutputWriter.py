# this is a file for making openfoam input file writing possible

class inputReader:

    def __init__(self):

        pass


class foamWriter:

    def __init__(self):

        print("hello there!")
        print("foam writer object initiated")

    def writeNewFile(self):

        pass


class test:

    def __init__(self):

        foamWriterObj = self.getFoamWriterObj()




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
