# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html
# https://stackoverflow.com/questions/31290738/create-a-triangular-mesh-using-delaunay-methods
# https://stackoverflow.com/questions/31290738/create-a-triangular-mesh-using-delaunay-methods

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from shapely.geometry import Polygon
from shapely.ops import triangulate




def getEquidistantPoints(p1, p2, parts):
# creates equidistant points
    xdir=np.linspace(p1[0], p2[0], parts+1)
    ydir=np.linspace(p1[1], p2[1], parts+1)
    return xdir, ydir
    #return zip(np.linspace(p1[0], p2[0], parts+1),
    #           np.linspace(p1[1], p2[1], parts+1))

points = np.array([[0, 0],
                  [40, 0],
                  [40, 30],
                  [60, 30], 
                  [60, 40], 
                  [40, 40],
                  [40, 80],
                  [0, 80]])


# Define the lines in terms of point numbers
lines=np.array([[0, 1],
                [1, 2],
                 [2, 3],
                 [3, 4],
                 [4, 5],
                 [5, 6],
                 [6, 7],
                 [7, 0]])


xf=np.array([0])
yf=np.array([0])

# Number of segments
seg=20#mm

for xy in lines:
  #print(xy[0])
  #new=list(getEquidistantPoints(tri.simplices[0], tri.simplices[1], 4))
  b=np.array(getEquidistantPoints(points[xy[0]], points[xy[1]], seg))
  xf=np.append(xf,b[0],axis=0)
  yf=np.append(yf,b[1],axis=0)

# loop over the lines
#for i in lines:
#    print(lines[i][0])
# create the final points np array
i=0

ppoints=np.empty((0, 2), float)
for x in xf:
  #ppoints=np.array([[0, 0],
  #                  [40, 0]])

  ppoints=np.append(ppoints,np.array([[xf[i], yf[i]]]), axis=0)
  polygon = Polygon( [ (0,0), (0,3), (5,3), (2,4), (6,4), (6,0) ])

  i=i+1
  #ppoints=np.array([float(xf[0]), float(yf[0])])

  
tri = Delaunay(ppoints)

# Delete rows of tri that are outside the boundary
print(tri.simplices)
#tri.simplices=np.delete(tri.simplices,10,0)
# tri.simplices=np.delete(tri.simplices,2,0)
# tri.simplices=np.delete(tri.simplices,2,0)


# The triplot() function in pyplot module of matplotlib library is used to draw a unstructured triangular grid as lines and/or markers
plt.triplot(ppoints[:,0], ppoints[:,1], tri.simplices)
plt.plot(ppoints[:,0], ppoints[:,1], 'o')
plt.show()


delauney=triangulate(polygon)
# Create a convex haul (minimum boundary containing all defined points, wie von Thiery Mal gezeigt)
#from scipy.spatial import ConvexHull, convex_hull_plot_2d
#rng = np.random.default_rng()
#points = rng.random((30, 2))   # 30 random points in 2-D
#hull = ConvexHull(points)
#plt.plot(points[:,0], points[:,1], 'o')
#for simplex in hull.simplices:
#    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')


print("end")


# Schwerpunkte der Dreiecke
# We can also compute barycentric coordinates in triangle 1 for these points:

# b = tri.transform[1,:2].dot(np.transpose(p - tri.transform[1,2]))
# np.c_[np.transpose(b), 1 - b.sum(axis=0)]

