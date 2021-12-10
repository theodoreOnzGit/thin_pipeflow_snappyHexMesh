class foamWriter:

    def __init__(self):

        print("foamWriter object initiated")

        self.setKinematicPressureInternalField(0)
        self.setVelocityInternalField(0,0,0)


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


    def writeFoamFileSection(self,fileName,fieldType):

        if fieldType == "vector":

            fieldType = "volVectorField"

        f = self.getAppendObj(fileName = fileName)

        f.write(r"FoamFile")
        f.write("\n")
        f.write(r"{")
        f.write("\n")
        f.write(r"    version     2.0;")
        f.write("\n")
        f.write(r"    format      ascii;")
        f.write("\n")
        f.write(r"    class       "+fieldType+";")
        f.write("\n")
        f.write(r"    object      "+fileName+";")
        f.write("\n")
        f.write(r"}")
        f.write("\n")

        f.close()

    def writeHeader2(self,fileName):

        f = self.getAppendObj(fileName = fileName)
        f.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //")
        f.write("\n")
        f.write(" ")
        f.write("\n")
        f.close()

    def writeKinematicPressureDimensions(self):

        
        f = self.getAppendObj(fileName = "p")

        f.write("dimensions      [0 2 -2 0 0 0 0];")
        f.write("\n")
        f.write(" ")
        f.write("\n")

        f.close()


    def writeVelocityDimensions(self):

        
        f = self.getAppendObj(fileName = "U")

        f.write("dimensions      [0 1 -1 0 0 0 0];")
        f.write("\n")
        f.write(" ")
        f.write("\n")

        f.close()

    def writeInternalField(self,fileName,internalFieldValue):

        internalFieldValue = str(internalFieldValue)

        f = self.getAppendObj(fileName = fileName)

        f.write("internalField   uniform " + internalFieldValue +";")
        f.write("\n")
        f.write(" ")
        f.write("\n")

        f.close()


    def writeVelocityInternalField(self):

        velocityField = self.getVelocityInternalField()

        ux = velocityField[0]
        uy = velocityField[1]
        uz = velocityField[2]

        internalFieldValue = "("+str(ux)+" "+str(uy)+" "+str(uz)+")"

        self.writeInternalField(fileName = "U", internalFieldValue = internalFieldValue)

    def writeKinematicPressureInternalField(self):

        self.writeInternalField(fileName = "p", internalFieldValue = self.getKinematicPressureInternalField())

    def writeVelocityFile(self):

        self.writeHeader(fileName = 'U')

        self.writeFoamFileSection(fileName = 'U', fieldType = 'volVectorField')

        self.writeHeader2(fileName = "U")

        self.writeVelocityDimensions()

        self.writeVelocityInternalField()

        print("velocity file written")

    def writeKinematicPressureFile(self):

        self.writeHeader(fileName = 'p')

        self.writeFoamFileSection(fileName = 'p', fieldType = 'volScalarField')

        self.writeHeader2(fileName = "p")

        self.writeKinematicPressureDimensions()

        self.writeKinematicPressureInternalField()


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


##### get and set functions are here #####


    def setVelocityInternalField(self,ux,uy,uz):

        self.ux = ux
        self.uy = uy
        self.uz = uz

    def getVelocityInternalField(self):

        return (self.ux,self.uy,self.uz)


    def setKinematicPressureInternalField(self,kinematicPressure):

        self.kinematicPressure = kinematicPressure

    def getKinematicPressureInternalField(self):

        return self.kinematicPressure
