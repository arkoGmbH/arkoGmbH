import numpy as np
import os

os.system('clear')

# We can treat this list of a list as a matrix
# /Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/env/bin/python

def RotMatX(theta):
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

def RotMatY(theta):
	#-------------------------------
	# 13.10.2021
	# Rotationsmatrix um X-Achse
	#
	#
	#--------------------------------
	# INPUT: Winkel phi in ° (wird in radiants umgerechnet)
	# OUTPUT: 3x3 Matrix mit rotationsfaktoren
	
	R=np.zeros((3,3)) # Double brackets for the zero matrix
	
	R[0,0]=np.cos(np.radians(theta))
	R[0,1]=0
	R[0,2]=np.sin(np.radians(theta))
	
	R[1,0]=0
	R[1,1]=1
	R[1,2]=-0
	
	R[2,0]=-np.sin(np.radians(theta))
	R[2,1]=0
	R[2,2]=np.cos(np.radians(theta))

	return R


def RotMatZ(theta):
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

def RotZeilenVektoren(M, alpha, dir):
	#-------------------------------
	# 13.10.2021
	# Mehrere Zeilenvektoren in eine m x 3 matrix rotieren
	#
	#
	#--------------------------------
	# INPUT:
	# - Matrix m x 3 mit Zeilenvektoren
	# - Winkel alpha mit dem rotiert werden soll
	# - Richtung dir um die rotiert werden soll 1= X-AChse, 2= Y-Achse, 3= Z-Achse
	# OUTPUT: N-Matrix mit rotierten Zeilenvektoren m x 3
	if dir==1:
		R = RotMatX(alpha)
	elif dir==2:
		R = RotMatY(alpha)
	elif dir==3:
		R = RotMatZ(alpha)
	else:
		print('Richtung dir für die Roationsmatrix wurde noch nicht definiert')
	numrows, ncols = M.shape
	V=np.zeros((3,1))
	N=np.zeros((numrows,3))
	print(V)
	i=0
	for i in range(0, numrows):
		R = RotMatZ(alpha)
		# Den jeweiligen Zeilenvektoren in einen Spaltenvektor umwandlen
		V[0,0] = M[i, 0]
		V[1,0] = M[i, 1]
		V[2,0] = M[i, 2]

		# Rotation durchführen
		U = np.matmul(R, V)

		# Die finale Zeilenvektoren matrix mit den rotierten Zeilenvektoren bilden
		N[i, 0] = U[0, 0]
		N[i, 1] = U[1, 0]
		N[i, 2] = U[2, 0]

	# Herausschreiben der rotierten Zeilenvektoren
	return N

def RotSpaltenVektoren(M, alpha, dir):
	#-------------------------------
	# 13.10.2021
	# Mehrere Spaltenvektoren in eine 3 x n matrix rotieren
	#
	#
	#--------------------------------
	# INPUT:
	# - Matrix 3 x n mit Spaltenvektoren
	# - Winkel alpha mit dem rotiert werden soll
	# - Richtung dir um die rotiert werden soll 1= X-AChse, 2= Y-Achse, 3= Z-Achse
	# OUTPUT: N-Matrix mit rotierten Spaltenvektoren 3 x n
	if dir==1:
		R = RotMatX(alpha)
	elif dir==2:
		R = RotMatY(alpha)
	elif dir==3:
		R = RotMatZ(alpha)
	else:
		print('Richtung dir für die Roationsmatrix wurde noch nicht definiert')
	numrows, ncols = M.shape
	V=np.zeros((3,1))
	N=np.zeros((3,ncols ))

	i=0
	for i in range(0, ncols):
		# Den jeweiligen Spaltenvektor erhalten
		V[0,0] = M[0, i]
		V[1,0] = M[1, i]
		V[2,0] = M[2, i]
		
		# Rotation durchführen
		U = np.matmul(R, V)

		# Die finale Zeilenvektoren matrix mit den rotierten Spaltenvektoren bilden
		N[0, i] = U[0, 0]
		N[1, i] = U[1, 0]
		N[2, i] = U[2, 0]

	# Herausschreiben der rotierten Zeilenvektoren
	return N

def test():
	# Testing -------------------------------
	theta=25
	a=RotMatX(theta)
	print(a)
	a=RotMatY(theta)
	print(a)
	a=RotMatZ(theta)
	print(a)

	MZl=np.matrix([[17,  1, 8],
			[		28,  1, 7],
			[		28,  1, 7],
			[		28,  1, 7]])

	MSpl=np.matrix([[17,  1, 8, 9, 7, 10,
			[		28,  1, 7, 9, 7, 10],
			[		28,  1, 7, 9, 7, 10],
			[		28,  1, 7, 9, 7, 10]]])


	MZl=np.random.rand(6,3)
	MSpl=np.random.rand(3,6)



	M1=RotZeilenVektoren(MZl,theta,1)
	M2=RotSpaltenVektoren(MSpl,theta,1)


	print(M1)
	print(M2)
	


#a=test()
print('End')