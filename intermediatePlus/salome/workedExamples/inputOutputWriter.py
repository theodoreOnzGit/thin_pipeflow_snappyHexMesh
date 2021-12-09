# this is a file for making openfoam input file writing possible

class inputReader:

    def __init__(self):

        pass


class foamWriter:

    def __init__(self):

        print("hello there!")
        print("foam writer object initiated")

    def getOverwriteObject(self):

        fileName = self.getFileName()

        return open(fileName,'w')

    def getAppendWriteObject(self):

        fileName = self.getFileName()

        return open(fileName,'a')

    def setFileName(self,fileName = 'file'):

        self.fileName = fileName

    def getFileName(self):

        return self.fileName

    def overwriteTest1(self):

        self.setFileName('test1')

        f = self.getOverwriteObject()

        f.write("this is test 1 for overwriting files")

    def appendTest1(self):

        f = self.getAppendWriteObject()

        f.write("hello, this is test 1 for appending")


    def appendTest2(self):

        f = self.getAppendWriteObject()

        # this one appends with a new line

        f.write("\n")

        f.write("hellow this is test 2 for appending")




    





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
