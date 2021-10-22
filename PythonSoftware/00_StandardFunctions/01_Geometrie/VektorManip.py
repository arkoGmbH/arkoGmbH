import numpy as np


# We can treat this list of a list as a matrix
# /Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python

def RotX(theta):
	#-------------------------------
	# 13.10.2021
	# Rotationsmatrix um X-Achse
	#
	#
	#--------------------------------
	# INPUT: Winkel phi in ° (wird in radiants umgerechnet)
	# OUTPUT: 3x3 Matrix mit rotationsfaktoren
	
	R=np.zeros((3,3)) # Double brackets for the zero matrix
	
	R[0,0]=1
	R[0,1]=0
	R[0,2]=0
	
	R[1,0]=0
	R[1,1]=np.cos(np.radians(theta))
	R[1,2]=-np.sin(np.radians(theta))
	
	R[2,0]=0
	R[2,1]=np.sin(np.radians(theta))
	R[2,2]=np.cos(np.radians(theta))

	return R

def RotY(theta):
	#-------------------------------
	# 13.10.2021
	# Rotationsmatrix um X-Achse
	#
	#
	#--------------------------------
	# INPUT: Winkel phi in ° (wird in radiants umgerechnet)
	# OUTPUT: 3x3 Matrix mit rotationsfaktoren
	
	R=np.zeros((3,3)) # Double brackets for the zero matrix
	
	R[0,0]=1
	R[0,1]=0
	R[0,2]=0
	
	R[1,0]=0
	R[1,1]=np.cos(np.radians(theta))
	R[1,2]=-np.sin(np.radians(theta))
	
	R[2,0]=0
	R[2,1]=np.sin(np.radians(theta))
	R[2,2]=np.cos(np.radians(theta))

	return R


def RotZ(theta):
	#-------------------------------
	# 13.10.2021
	# Rotationsmatrix um Z-Achse
	#
	#
	#--------------------------------
	# INPUT: Winkel phi in ° (wird in radiants umgerechnet)
	# OUTPUT: 3x3 Matrix mit rotationsfaktoren

	R=np.zeros((3,3)) # Double brackets for the zero matrix

	R[0,0]=np.cos(np.radians(theta))
	R[0,1]=-np.sin(np.radians(theta))
	R[0,2]=0
	
	R[1,0]=np.sin(np.radians(theta))
	R[1,1]=np.cos(np.radians(theta))
	R[1,2]=0
	
	R[2,0]=0
	R[2,1]=0
	R[2,2]=1

	return R



theta=25

a=RotX(theta)
print(a)
a=RotY(theta)
print(a)
a=RotZ(theta)
print(a)