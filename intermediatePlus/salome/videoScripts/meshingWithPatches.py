#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.7.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/SALOME-9.7.0-native-UB20.04-SRC/thin_pipeflow_snappyHexMesh/intermediatePlus/salome/videoScripts')

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
Vertex_1 = geompy.MakeVertex(0, 0, -150)
Vertex_2 = geompy.MakeVertex(0, 0, 150)
Vector_1 = geompy.MakeVector(Vertex_1, Vertex_2)
Cylinder2 = geompy.MakeCylinder(Vertex_1, Vector_1, 100, 300)
outlet = geompy.CreateGroup(Cylinder2, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [10])
wall = geompy.CreateGroup(Cylinder2, geompy.ShapeType["FACE"])
geompy.UnionIDs(wall, [3])
inlet = geompy.CreateGroup(Cylinder2, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, [12])
[outlet, wall, inlet] = geompy.GetExistingSubObjects(Cylinder2, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vector_1, 'Vector_1' )
geompy.addToStudy( Cylinder2, 'Cylinder2' )
geompy.addToStudyInFather( Cylinder2, outlet, 'outlet' )
geompy.addToStudyInFather( Cylinder2, wall, 'wall' )
geompy.addToStudyInFather( Cylinder2, inlet, 'inlet' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

cylinder2Mesh = smesh.Mesh(Cylinder2)
NETGEN_1D_2D_3D = cylinder2Mesh.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
outlet_1 = cylinder2Mesh.GroupOnGeom(outlet,'outlet',SMESH.FACE)
wall_1 = cylinder2Mesh.GroupOnGeom(wall,'wall',SMESH.FACE)
inlet_1 = cylinder2Mesh.GroupOnGeom(inlet,'inlet',SMESH.FACE)
isDone = cylinder2Mesh.Compute()
[ outlet_1, wall_1, inlet_1 ] = cylinder2Mesh.GetGroups()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(wall_1, 'wall')
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(cylinder2Mesh.GetMesh(), 'cylinder2Mesh')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
