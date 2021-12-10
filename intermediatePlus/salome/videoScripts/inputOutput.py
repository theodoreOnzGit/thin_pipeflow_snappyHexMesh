class foamWriter:

    def __init__(self):

        print("foamWriter object initiated")


    def writeHeader(self,fileName):

        f = self.getOverwriteObj(fileName = fileName)

        f.write(r"/*--------------------------------*- C++ -*----------------------------------*\//")
        f.write("\n")
        f.close()

        f = self.getAppendObj(fileName = fileName)

        f.write(r"| =========                 |                                                 | ")
        f.write("\n")
        f.write(r"| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           | ")
        f.write("\n")
        f.write(r"|  \\    /   O peration     | input file made by foamWriter Object python     | ")
        f.write("\n")
        f.write(r"|   \\  /    A nd           | Website:  www.openfoam.com                      | ")
        f.write("\n")
        f.write(r"|    \\/     M anipulation  |                                                 | ")
        f.write("\n")
        f.write(r"\*---------------------------------------------------------------------------*/ ")
        f.write("\n")

        f.close()

    def writeVelocityFile(self):

        self.writeHeader(fileName = 'U')

        print("velocity file written")

    def writeKinematicPressureFile(self):

        self.writeHeader(fileName = 'p')

        print("pressure file written")


    def getOpenObj(self,fileName,mode):

        f = open(fileName,mode)

        return f

    def getOverwriteObj(self,fileName):

        f = self.getOpenObj(fileName = fileName, mode = "w")

        return f

    def getAppendObj(self,fileName):

        f = self.getOpenObj(fileName = fileName, mode = "a")

        return f
