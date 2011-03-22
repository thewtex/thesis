from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

a = 3
b = 2
c = 1

x = a * np.outer(np.cos(u), np.cosh(v))
y = b * np.outer(np.sin(u), np.sinh(v))
z = c * np.outer(np.ones(np.size(u)), np.sinh(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
#ax.set_xlim3d(-a, a)
#ax.set_ylim3d(-a, a)
#ax.set_zlim3d(-a, a)
ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$x_3$')

plt.savefig('../../images/hyperboloid_one_sheet.png', dpi=150)
plt.show()
