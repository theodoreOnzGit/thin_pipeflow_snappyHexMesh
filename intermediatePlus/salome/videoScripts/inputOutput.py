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


    def writeFoamFileSection(self,fileName,fieldType,objectName):

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
        f.write(r"    object      "+objectName+";")
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

    def writeOutro(self,fileName):

        f = self.getAppendObj(fileName = fileName)
        f.write("// ************************************************************************* //")
        f.write("\n")
        f.close()

    def writeKinematicPressureDimensions(self):

        
        f = self.getAppendObj(fileName = self.getFilePath()+"p")

        f.write("dimensions      [0 2 -2 0 0 0 0];")
        f.write("\n")
        f.write(" ")
        f.write("\n")

        f.close()


    def writeVelocityDimensions(self):

        
        f = self.getAppendObj(fileName = self.getFilePath()+"U")

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

        self.writeInternalField(fileName = self.getFilePath()+"U", internalFieldValue = internalFieldValue)

    def writeKinematicPressureInternalField(self):

        self.writeInternalField(fileName = self.getFilePath()+"p", internalFieldValue = self.getKinematicPressureInternalField())

    def writeVelocityFile(self):

        self.writeHeader(fileName = self.getFilePath()+'U')

        self.writeFoamFileSection(fileName = self.getFilePath()+'U', fieldType = 'volVectorField',objectName = 'U')

        self.writeHeader2(fileName = self.getFilePath()+"U")

        self.writeVelocityDimensions()

        self.writeVelocityInternalField()

        self.writeBoundaryFieldU()

        self.writeOutro(fileName = self.getFilePathU())


        print("velocity file written")

    def writeKinematicPressureFile(self):

        self.writeHeader(fileName = self.getFilePath()+'p')

        self.writeFoamFileSection(fileName = self.getFilePath()+'p', fieldType = 'volScalarField', objectName = 'p')

        self.writeHeader2(fileName = self.getFilePath()+"p")

        self.writeKinematicPressureDimensions()

        self.writeKinematicPressureInternalField()

        self.writeBoundaryFieldP()

        self.writeOutro(fileName = self.getFilePathP())

        print("pressure file written")



##### this section is for boundary fields #####

    def writeBoundaryFieldU(self):

        self.writeBoundaryField(fileName =  self.getFilePath()+'U', objectName = 'U')

    def writeBoundaryFieldP(self):

        self.writeBoundaryField(fileName =  self.getFilePath()+'p', objectName = 'p')




    def writeBoundaryField(self,fileName,objectName):

        self.writeBoundaryFieldOpener(fileName = fileName)

        self.setInletBoundaryConditions(objectName = objectName)
        self.writePatch(fileName = fileName)

        self.setOutletBoundaryConditions(objectName = objectName)
        self.writePatch(fileName = fileName)

        self.setWallBoundaryConditions(objectName = objectName)
        self.writePatch(fileName = fileName)

        self.writeBoundaryFieldCloser(fileName = fileName)



    def writeBoundaryFieldOpener(self,fileName):

        f = self.getAppendObj(fileName = fileName)

        f.write("boundaryField")
        f.write("\n")
        f.write("{")
        f.write("\n")

        f.close()

    def writeBoundaryFieldCloser(self,fileName):


        f = self.getAppendObj(fileName = fileName)

        f.write("}")
        f.write("\n")
        f.write(" ")
        f.write("\n")

        f.close()

    def writePatch(self,fileName):

        self.writePatchOpener(fileName = fileName, patchName = self.getPatchName())

        self.writePatchType(fileName = fileName , patchType = self.getPatchType())

        self.writePatchValue(fileName = fileName , patchValue = self.getPatchValue())

        self.writePatchCloser(fileName = fileName)




    def writePatchOpener(self,fileName,patchName):

        f = self.getAppendObj(fileName = fileName)

        f.write('    '+patchName)
        f.write("\n")
        f.write("    {")
        f.write("\n")

        f.close()


    def writePatchType(self,fileName,patchType='fixedValue'):

        f = self.getAppendObj(fileName = fileName)

        f.write('        '+'type'+'             '+patchType+';')
        f.write("\n")

        f.close()


    def writePatchValue(self,fileName,patchValue='uniform 0'):

        if patchValue == 'nil':
            return None

        f = self.getAppendObj(fileName = fileName)

        f.write('        '+'value'+'            '+patchValue+';')
        f.write("\n")

        f.close()


    def writePatchCloser(self,fileName):


        f = self.getAppendObj(fileName = fileName)

        f.write("    }")
        f.write("\n")
        f.write(" ")
        f.write("\n")
        f.close()

##### these are functions to help set the right boundary conditions #####

    def setInletBoundaryConditions(self,objectName,patchName = 'inlet'):

        self.setPatchName(patchName)

        if objectName == 'U':
            self.setPatchType('fixedValue')
            self.setPatchValue('uniform (0 0 1)')

        elif objectName == 'p':
            self.setPatchType('zeroGradient')
            self.setPatchValue()



    def setOutletBoundaryConditions(self,objectName,patchName = 'outlet'):

        self.setPatchName(patchName)

        if objectName == 'U':
            self.setPatchType('zeroGradient')
            self.setPatchValue()

        elif objectName == 'p':
            self.setPatchType('fixedValue')
            self.setPatchValue('uniform 10000')



    def setWallBoundaryConditions(self,objectName,patchName = 'wall'):

        self.setPatchName(patchName)

        if objectName == 'U':
            self.setPatchType('noSlip')
            self.setPatchValue()

        elif objectName == 'p':
            self.setPatchType('zeroGradient')
            self.setPatchValue()

##### get and set functions are here #####

    def getOpenObj(self,fileName,mode):

        f = open(fileName,mode)

        return f

    def getOverwriteObj(self,fileName):

        f = self.getOpenObj(fileName = fileName, mode = "w")

        return f

    def getAppendObj(self,fileName):

        f = self.getOpenObj(fileName = fileName, mode = "a")

        return f

    def getReadObj(self,fileName):

        f = self.getOpenObj(fileName = fileName, mode = "r")

        return f

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

    def getCurrentDir(self):

        import os

        return os.getcwd()

    def getFilePath(self):

        localFilePath =  '/thin_pipeflow_snappyHexMesh/intermediatePlus/salome/videoScripts/'

        return self.getCurrentDir() + localFilePath

    def getFilePathU(self):

        return self.getFilePath() + 'U'

    def getFilePathP(self):

        return self.getFilePath() + 'p'


    def setPatchName(self,patchName):

        self.patchName = patchName

    def getPatchName(self):

        return self.patchName

    def setPatchType(self,patchType):

        self.patchType = patchType

    def getPatchType(self):

        return self.patchType

    def setPatchValue(self,patchValue='nil'):

        self.patchValue = patchValue

    def getPatchValue(self):

        return self.patchValue




##### here are functions/methods to read files #####

    def readAndPrintFile(self,fileName, mode = 2):

        f = self.getReadObj(fileName = fileName)

        if mode == 1:

            for line in f:
                print(line)

        elif mode == 2:

            contents = f.read()
            print(contents)




