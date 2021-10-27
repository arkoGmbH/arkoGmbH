
# https://documen.tician.de/meshpy/


from meshpy.tet import MeshInfo, build
import pyvtk

from matplotlib import pyplot as plt

mesh_info = MeshInfo()

mesh_info.set_points([
    (0,0,0), (2,0,0), (2,2,0), (0,2,0),
    (0,0,12), (2,0,12), (2,2,12), (0,2,12),
    ])




a=([
    (0,0,0), (2,0,0), (2,2,0), (0,2,0),
    (0,0,12), (2,0,12), (2,2,12), (0,2,12),
    ])


plt.scatter([i[1] for i in a],[i[2] for i in a])


mesh_info.set_facets([
    [0,1,2,3],
    [4,5,6,7],
    [0,4,5,1],
    [1,5,6,2],
    [2,6,7,3],
    [3,7,4,0],
    ])

    
mesh = build(mesh_info)
print("Mesh Points:")
for i, p in enumerate(mesh.points):
    print(i, p)
print("Point numbers in tetrahedra:")
for i, t in enumerate(mesh.elements):
    print(i, t)
mesh.write_vtk("test.vtk")

print("End")