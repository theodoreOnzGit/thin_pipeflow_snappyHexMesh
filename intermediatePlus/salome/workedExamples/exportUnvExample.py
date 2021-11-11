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
### SHAPER component
###

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
model.end()

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
geomObj_5 = geompy.MakeVertex(0, 0, 0)
geomObj_6 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_7 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_8 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_9 = geompy.MakeCylinderRH(100, 300)
geomObj_10 = geompy.MakeVertex(0, 0, 0)
geomObj_11 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_12 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_13 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_14 = geompy.MakeCylinderRH(100, 300)
geomObj_15 = geompy.MakeVertex(0, 0, 0)
geomObj_16 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_17 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_18 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_19 = geompy.MakeCylinderRH(100, 300)
geomObj_20 = geompy.MakeVertex(0, 0, 0)
geomObj_21 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_22 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_23 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_24 = geompy.MakeVertex(0, 0, 0)
geomObj_25 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_26 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_27 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_28 = geompy.MakeCylinderRH(100, 300)
geomObj_29 = geompy.MakeVertex(0, 0, 0)
geomObj_30 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_31 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_32 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_33 = geompy.MakeVertex(0, 0, 0)
geomObj_34 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_35 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_36 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_37 = geompy.MakeCylinderRH(100, 300)
geomObj_38 = geompy.MakeVertex(0, 0, 0)
geomObj_39 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_40 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_41 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_42 = geompy.MakeVertex(0, 0, 0)
geomObj_43 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_44 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_45 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_46 = geompy.MakeCylinderRH(100, 300)
geomObj_47 = geompy.MakeVertex(0, 0, 0)
geomObj_48 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_49 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_50 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_51 = geompy.MakeVertex(0, 0, 0)
geomObj_52 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_53 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_54 = geompy.MakeVectorDXDYDZ(0, 0, 1)
geomObj_55 = geompy.MakeCylinderRH(100, 300)
geomObj_56 = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
cylinder1 = geompy.MakeCylinderRH(100, 300)
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( cylinder1, 'cylinder1' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

NETGEN_3D_Parameters_1 = smesh.CreateHypothesis('NETGEN_Parameters', 'NETGENEngine')
NETGEN_3D_Parameters_1.SetMaxSize( 41.2311 )
NETGEN_3D_Parameters_1.SetMinSize( 17.4311 )
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 4 )
NETGEN_3D_Parameters_1.SetChordalError( -1 )
NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_1.SetCheckChartBoundary( 3 )
NETGEN_1D_2D_3D = smesh.CreateHypothesis('NETGEN_2D3D', 'NETGENEngine')
try:
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
try:
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
NETGEN_Parameters = smesh.CreateHypothesis('NETGEN_Parameters', 'libNETGENEngine.so')
NETGEN_Parameters.SetMaxSize( 41.2311 )
NETGEN_Parameters.SetMinSize( 17.4311 )
NETGEN_Parameters.SetSecondOrder( 0 )
NETGEN_Parameters.SetOptimize( 1 )
NETGEN_Parameters.SetFineness( 4 )
NETGEN_Parameters.SetChordalError( -1 )
NETGEN_Parameters.SetChordalErrorEnabled( 0 )
NETGEN_Parameters.SetUseSurfaceCurvature( 1 )
NETGEN_Parameters.SetFuseEdges( 1 )
NETGEN_Parameters.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_1_1 = smesh.CreateHypothesis('NETGEN_Parameters', 'libNETGENEngine.so')
NETGEN_3D_Parameters_1_1.SetMaxSize( 41.2311 )
NETGEN_3D_Parameters_1_1.SetMinSize( 17.4311 )
NETGEN_3D_Parameters_1_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1_1.SetFineness( 4 )
NETGEN_3D_Parameters_1_1.SetChordalError( -1 )
NETGEN_3D_Parameters_1_1.SetChordalErrorEnabled( 0 )
NETGEN_3D_Parameters_1_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1_1.SetQuadAllowed( 0 )
mesh1 = smesh.Mesh(cylinder1)
status = mesh1.AddHypothesis(NETGEN_1D_2D_3D)
NETGEN_3D_Parameters_1_2 = smesh.CreateHypothesis('NETGEN_Parameters', 'libNETGENEngine.so')
status = mesh1.AddHypothesis(NETGEN_3D_Parameters_1_2)
NETGEN_3D_Parameters_1_2.SetMaxSize( 41.2311 )
NETGEN_3D_Parameters_1_2.SetMinSize( 17.4311 )
NETGEN_3D_Parameters_1_2.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1_2.SetOptimize( 1 )
NETGEN_3D_Parameters_1_2.SetFineness( 4 )
NETGEN_3D_Parameters_1_2.SetChordalError( -1 )
NETGEN_3D_Parameters_1_2.SetChordalErrorEnabled( 0 )
NETGEN_3D_Parameters_1_2.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1_2.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1_2.SetQuadAllowed( 0 )
isDone = mesh1.Compute()
try:
  mesh1.ExportUNV( r'/root/salome/SALOME-9.7.0-native-UB20.04-SRC/thin_pipeflow_snappyHexMesh/intermediatePlus/salome/workedExamples/mesh1.unv' )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D, 'NETGEN 1D-2D-3D')
smesh.SetName(NETGEN_Parameters, 'NETGEN_Parameters')
smesh.SetName(NETGEN_3D_Parameters_1_1, 'NETGEN 3D Parameters_1')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(NETGEN_3D_Parameters_1_2, 'NETGEN 3D Parameters_1')
smesh.SetName(mesh1.GetMesh(), 'mesh1')

###
### SHAPERSTUDY component
###


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
