import netgen as nt
import netgen.gui
from netgen.geom2d import SplineGeometry

geo = nt.geom2d.SplineGeometry()
p1 = geo.AppendPoint (0,0)
p2 = geo.AppendPoint (1,0)
p3 = geo.AppendPoint (1,1)
p4 = geo.AppendPoint (0,1)


geo.Append (["line", p1, p2])
geo.Append (["line", p2, p3])
geo.Append (["line", p3, p4])
geo.Append (["line", p4, p1])

# generate a mesh
mesh = geo.GenerateMesh (maxh=0.1)

# iterate over points and elements of the mesh:

for p in mesh.Points():
 x,y,z = p.p
 print ("x = ", x, "y = ", y)
 for el in mesh.Elements2D():
   print (el.vertices)