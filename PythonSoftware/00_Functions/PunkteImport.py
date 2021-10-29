# Importieren der Punkte für das Flügelprofil

import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append(SdrPath='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/GitHub/arkoGmbH/PythonSoftware/00_Functions")
import VektorManip

def ReadFile(FullPath):
    plt.close('all')
    filename=FullPath

    f=open(filename,"r")
    lines=f.readlines()
    xvalues=[]
    yvalues=[]
    zvalues=[]

    for line in lines:#
        xvalues.append(float(line.split('\t')[0])) # Input in double konvertieren (erste Spalte)
        yvalues.append(float(line.split('\t')[1])) # Input in double konvertieren (zweite Spalte)
        zvalues.append(float(line.split('\t')[2])) 
    f.close()

    xvs=np.array(xvalues)#.reshape((-1, 1))
    yvs=np.array(yvalues)#.reshape((-1, 1))
    zvs=np.array(yvalues)#.reshape((-1, 1))

    M=np.matrix([ xvalues,
        yvalues,
        zvalues])

    # Close file
    f.close()

    
    print("---File processing ended---")
    return M


def test():
    FullPath='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/553_3DPoints/02_P-51Airfoil/P-51D_Enhanced.csv'
    M=ReadFile(FullPath)
    A=RotSpaltenVektoren(M,15,1) # Um X-Richtung
    B=RotSpaltenVektoren(A,30,2) # Um Y-Richtung
    C=RotSpaltenVektoren(B,10,3) # Um Z-Richtung

    numrows, ncols = C.shape
    x=np.zeros((1,ncols))
    y=np.zeros((1,ncols))

    x[0,:]=C[0,:]
    y[0,:]=C[1,:]

    XL=x.tolist()
    YL=y.tolist()

    fig = plt.Figure(figsize=(3, 2), dpi=100)
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(XL[0], YL[0])  # Plot some data on the axes.
    plt.show()


#a=test()
print('END')