#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.7.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/root/salome/SALOME-9.7.0-native-UB20.04-SRC/thin_pipeflow_snappyHexMesh/intermediatePlus/salome/workedExamples')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

geomObj_1 = geompy.MakeVertex(0, 0, 0)
geomObj_2 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_3 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_4 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_5 = geompy.MakeCylinderRH(100, 300)
[Cylinder_1, Group_1, inlet] = geompy.GetExistingSubObjects(geomObj_5, False)
Cylinder_1 = geompy.MakeCylinderRH(100, 300)
inlet = geompy.CreateGroup(Cylinder_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, [3])
outlet = geompy.CreateGroup(Cylinder_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [10])
[inlet, outlet, Group_1] = geompy.GetExistingSubObjects(Cylinder_1, False)
Group_1 = geompy.CreateGroup(Cylinder_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_1, [3])
Vertex_1 = geompy.MakeVertex(0, 0, 0)
cylinderBottomPoint = geompy.MakeVertex(0, 0, -150)
Vector_1 = geompy.MakeVector(cylinderBottomPoint, Vertex_1)
Cylinder_2 = geompy.MakeCylinder(cylinderBottomPoint, Vector_1, 100, 300)
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudyInFather( Cylinder_1, Group_1, 'Group_1' )
geompy.addToStudyInFather( Cylinder_1, inlet, 'inlet' )
geompy.addToStudyInFather( Cylinder_1, outlet, 'outlet' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( cylinderBottomPoint, 'cylinderBottomPoint' )
geompy.addToStudy( Vector_1, 'Vector_1' )
geompy.addToStudy( Cylinder_2, 'Cylinder_2' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

NETGEN_1D_2D_3D = smesh.CreateHypothesis('NETGEN_2D3D', 'libNETGENEngine.so')
Mesh_1 = smesh.Mesh(Cylinder_1)
MG_Hexa = Mesh_1.Hexahedron(algo=smeshBuilder.MG_Hexa)
inlet_1 = Mesh_1.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outlet_1 = Mesh_1.GroupOnGeom(outlet,'outlet',SMESH.FACE)
Group_1_1 = Mesh_1.GroupOnGeom(Group_1,'Group_1',SMESH.FACE)
isDone = Mesh_1.Compute()
[ inlet_1, outlet_1, Group_1_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ inlet_1, outlet_1, Group_1_1 ] = Mesh_1.GetGroups()
status = Mesh_1.RemoveHypothesis(MG_Hexa)
Cartesian_3D = Mesh_1.BodyFitted()
isDone = Mesh_1.Compute()
[ inlet_1, outlet_1, Group_1_1 ] = Mesh_1.GetGroups()
status = Mesh_1.RemoveHypothesis(Cartesian_3D)
status = Mesh_1.AddHypothesis(NETGEN_1D_2D_3D)
isDone = Mesh_1.Compute()
[ inlet_1, outlet_1, Group_1_1 ] = Mesh_1.GetGroups()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D, 'NETGEN 1D-2D-3D')
smesh.SetName(Cartesian_3D.GetAlgorithm(), 'Cartesian_3D')
smesh.SetName(MG_Hexa.GetAlgorithm(), 'MG-Hexa')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(Group_1_1, 'Group_1')
smesh.SetName(inlet_1, 'inlet')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
