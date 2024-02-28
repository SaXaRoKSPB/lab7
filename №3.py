from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-10, 10)
y = np.linspace(-0.5, 0.5)
z = np.tan(x+y)

line = plt.figure()
graph_3D = line.add_subplot(projection='3d')
graph_3D.plot(x, y, z)

graph_3D.set_xlabel('x')
graph_3D.set_ylabel('y')
graph_3D.set_zlabel('z')

plt.show()
