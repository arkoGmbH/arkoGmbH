#ttps://alpynepyano.github.io/healthyNumerics/posts/cfd-01-rectangular-grid-genereation-python.html

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mclr
from matplotlib import path
import sqlite3
from scipy.spatial import Delaunay

# Define the profile points
points = np.array([[0, 0],
                  [40, 0],
                  [40, 20],
                  [60, 30], 
                  [60, 40], 
                  [40, 40],
                  [40, 80],
                  [0, 80],
                   [0, 0]])


# Connect/Create DB in which the properties are stored
DBName='Profileigenschaften.db'
Path='/Users/newmini/Documents/00_All/3_Arbeit/3_arko_GmbH/9_Projects/01_arko_GmbH/549_Funktionen_Berechnung/07_TrägheitsTool/PythonProject/'
PathName=Path+DBName
con = sqlite3.connect(PathName)


nx = 70; ny = 85

number=10

#---- set the 1-dimensional arrays in x- and y-direction
ix = np.linspace(-10,nx,num=number)
iy = np.linspace(-10,ny,num=number)

#---- use the outer product of 2 vectors ----------- The outer product creates an m x n matrix
x = np.outer(ix,np.ones_like(iy))  # X = ix.T * ones(iy)
y = np.outer(np.ones_like(ix),iy)  # Y = ones(ix) * iy.T

x1d=np.ndarray.flatten(x)
y1d=np.ndarray.flatten(y)

# Delete row from array
#x1d=np.delete(x1d,7,0)
#y1d=np.delete(y1d,7,0)

# Find if point is within the surface or not
# https://stackoverflow.com/questions/31542843/inpolygon-for-python-examples-of-matplotlib-path-path-contains-points-method
#from matplotlib import path
bnd=[(0,0), (0, 1), (1, 1), (1, 0)]
#Create boundary from points in form of a tuple
bnd2=[tuple(points[i]) for i, item in enumerate(points)]
p = path.Path(bnd2)  # square with legs length 1 and bottom left corner at the origin


xf=np.empty([0,0])
yf=np.empty([0,0])
#xf=np.empty([1,1])
#yf=np.empty([1,1])

Deleted=list()

for i, item in enumerate(x1d):
    a=p.contains_points([(x1d[i], y1d[i])]) # List with one tuple of x,y coordinates
    if a[0]==True:
        xf=np.append(xf, x1d[i])
        yf=np.append(yf, y1d[i])
        Deleted.append([x1d[i],y1d[i]])

#x=np.delete(x[5],5,0)
#np.delete(x[10],10,0)

#y=np.delete(y[5],5,0)
#y=np.delete(y[10],10,0)
plt.figure(num='Profil Eigenschaften')
# Mesh ploten
plt.plot(xf, yf, '.', color='black',markersize=0.5);
# Querschnittsgeometrie ploten
plt.plot(points[:,0], points[:,1], color='r', marker = 'o',linestyle='solid',linewidth=2, markersize=3, markerfacecolor="w", markeredgecolor="r")

# Triangulation
xytr=np.vstack((xf, yf)).T
tri = Delaunay(xytr)
plt.triplot(xytr[:,0], xytr[:,1], tri.simplices)

# Skalieren
scale_factor = 1.1

xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()

plt.xlim(xmin * scale_factor, xmax * scale_factor)
plt.ylim(ymin * scale_factor, ymax * scale_factor)
plt.xlabel("[mm]")
plt.ylabel("[mm]")

plt.title("")


plt.show()




#====  The following is for the grafics ===============
#z =np.sqrt(x*x + y*y) # set a fancy Z function

#fig = plt.figure(figsize=(22,11)) 
#ax1 = fig.add_subplot(121)
##ax1.pcolormesh(x, y, z, edgecolors='w',cmap="plasma")

#ax1.set_aspect('equal')



#myCmap = mclr.ListedColormap(['white','white'])
#ax4 = fig.add_subplot(122)
#ax4.pcolormesh(x, y, np.zeros_like(x), edgecolors='k', lw=1, cmap=myCmap)
#ax4.set_aspect('equal')
#plt.show()