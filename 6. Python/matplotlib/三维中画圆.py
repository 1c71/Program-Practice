from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Circle
 
fig = plt.figure()
ax = fig.gca(projection = '3d')
 
 
cir = Circle((50,50),radius = 15,facecolor='none',edgecolor='red')
ax.add_patch(cir)
art3d.pathpatch_2d_to_3d(cir, z=0, zdir="z")
cir = Circle((50,50),radius = 30,facecolor='none',edgecolor='g',linestyle ='dashed')
ax.add_patch(cir)
art3d.pathpatch_2d_to_3d(cir, z=0, zdir="z")
 
cir = Circle((50,50),radius = 45,facecolor='none',edgecolor='y')
ax.add_patch(cir)
art3d.pathpatch_2d_to_3d(cir, z=0, zdir="z")
 
ax.set_xlim3d(0, 100)
ax.set_ylim3d(0, 100)
ax.set_zlim3d(0, 0.05)
 
 
plt.show()
















