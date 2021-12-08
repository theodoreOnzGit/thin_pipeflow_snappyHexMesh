#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.7.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/SALOME-9.7.0-native-UB20.04-SRC/thin_pipeflow_snappyHexMesh/intermediatePlus/salome/workedExamples')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_1 = geompy.MakeVertex(0, 0, 0)
OX_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY_1 = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ_1 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_2 = geompy.MakeVertex(0, 0, 150)
geomObj_3 = geompy.MakeVertex(0, 0, -150)
geomObj_4 = geompy.MakeVector(geomObj_3, geomObj_2)
cylinder2 = geompy.MakeCylinder(geomObj_3, geomObj_4, 100, 300)
[geomObj_5,geomObj_6,geomObj_7] = geompy.SubShapeAllSortedCentres(cylinder2, geompy.ShapeType["FACE"])
[geomObj_8,geomObj_9,geomObj_10] = geompy.SubShapeAllSortedCentres(cylinder2, geompy.ShapeType["FACE"])
geomObj_11 = geompy.CreateGroup(cylinder2, geompy.ShapeType["FACE"])
geomObj_12 = geompy.CreateGroup(cylinder2, geompy.ShapeType["FACE"])
inlet = geompy.CreateGroup(cylinder2, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, [12])
wall = geompy.CreateGroup(cylinder2, geompy.ShapeType["FACE"])
geompy.UnionIDs(wall, [3])
outlet = geompy.CreateGroup(cylinder2, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [10])
[geomObj_11, geomObj_5, geomObj_6, geomObj_7, geomObj_12, geomObj_8, geomObj_9, geomObj_10, inlet, wall, outlet] = geompy.GetExistingSubObjects(cylinder2, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( OX_1, 'OX' )
geompy.addToStudy( OY_1, 'OY' )
geompy.addToStudy( OZ_1, 'OZ' )
geompy.addToStudy( cylinder2, 'cylinder2' )
geompy.addToStudyInFather( cylinder2, inlet, 'inlet' )
geompy.addToStudyInFather( cylinder2, wall, 'wall' )
geompy.addToStudyInFather( cylinder2, outlet, 'outlet' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

meshWithFaces = smesh.Mesh(cylinder2)
NETGEN_1D_2D_3D = meshWithFaces.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
#Group_1 = meshWithFaces.GroupOnGeom(__NOT__Published__Object__,'',SMESH.FACE)
#Group_2 = meshWithFaces.GroupOnGeom(__NOT__Published__Object__,'',SMESH.FACE)
#Group_3 = meshWithFaces.GroupOnGeom(__NOT__Published__Object__,'',SMESH.FACE)
#Group_4 = meshWithFaces.GroupOnGeom(__NOT__Published__Object__,'',SMESH.FACE)
#Group_5 = meshWithFaces.GroupOnGeom(__NOT__Published__Object__,'',SMESH.FACE)
#Group_6 = meshWithFaces.GroupOnGeom(__NOT__Published__Object__,'',SMESH.FACE)
inlet_1 = meshWithFaces.GroupOnGeom(inlet,'inlet',SMESH.FACE)
wall_1 = meshWithFaces.GroupOnGeom(wall,'wall',SMESH.FACE)
outlet_1 = meshWithFaces.GroupOnGeom(outlet,'outlet',SMESH.FACE)
isDone = meshWithFaces.Compute()
[ Group_1, Group_2, Group_3, Group_4, Group_5, Group_6, inlet_1, wall_1, outlet_1 ] = meshWithFaces.GetGroups()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(wall_1, 'wall')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(Group_1, 'Group_1')
smesh.SetName(Group_2, 'Group_2')
smesh.SetName(Group_3, 'Group_3')
smesh.SetName(Group_4, 'Group_4')
smesh.SetName(Group_5, 'Group_5')
smesh.SetName(Group_6, 'Group_6')
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(meshWithFaces.GetMesh(), 'meshWithFaces')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
