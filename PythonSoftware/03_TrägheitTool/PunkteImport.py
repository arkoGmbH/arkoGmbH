# Importieren der Punkte für das Flügelprofil

import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/00_StandardFunctions/01_Geometrie")
from VektorManip import RotSpaltenVektoren

def ReadFile(FullPath):
    plt.close('all')
    filename=FullPath

    f=open(filename,"r")
    lines=f.readlines()
    xvalues=[]
    yvalues=[]
    zvalues=[]

    for line in lines:#
        xvalues.append(float(line.split(',')[0])) # Input in double konvertieren (erste Spalte)
        yvalues.append(float(line.split(',')[1])) # Input in double konvertieren (zweite Spalte)
        zvalues.append(float(line.split(',')[2])) 
    f.close()

    xvs=np.array(xvalues)#.reshape((-1, 1))
    yvs=np.array(yvalues)#.reshape((-1, 1))
    zvs=np.array(yvalues)#.reshape((-1, 1))

    M=np.array([ xvs,
                yvs,
                zvs])

    # Close file
    f.close()

    
    print("---File processing ended---")
    return M

fig = plt.Figure(figsize=(3, 2), dpi=100)
FullPath='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/553_3DPoints/02_P-51Airfoil/P-51D_Root_airfoil.csv'
M=ReadFile(FullPath)
A=RotSpaltenVektoren(M,10,1)
B=RotSpaltenVektoren(A,20,2)

numrows, ncols = A.shape
x=np.zeros((1,ncols))
y=np.zeros((1,ncols))

x[0,:]=B[0,:]
y[0,:]=B[1,:]

plt.scatter(x, y, alpha=0.5)
plt.show()