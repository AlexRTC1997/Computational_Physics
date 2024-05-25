import numpy as np
import matplotlib.pyplot as plt
from magpylib.source.magnet import Cylinder, Box
from magpylib import Collection, displaySystem

# [1] Create magnets
x1 = Box(mag=(0, 0, 600), dim=(3, 3, 3), pos=(-4, 0, 3))
x2 = Cylinder(mag=(0, 0, 500), dim=(3, 5))

# [2] Create collection
c = Collection(x1, x2)

# [3] Manipulate magnets individually
x1.rotate(45, (0, 1, 0), anchor=(0, 0, 0))
x2.move((5, 0, -4))

# [4] Manipulate collection
c.move((-2, 0, 0))

# [5] Calculate B-field on a grid
xs = np.linspace(-10, 10, 33)
zs = np.linspace(-10, 10, 44)
POS = np.array([(x, 0, z) for z in zs for x in xs])
Bs = c.getB(POS).reshape(44, 33, 3)  # VECTORIZED

# [6] Create figure
fig = plt.figure(figsize=(9, 5))
ax1 = fig.add_subplot(121, projection='3d')  # 3D-axis
ax2 = fig.add_subplot(122)  # 2D-axis

# [7] Display system geometry on ax1
displaySystem(c, subplotAx=ax1, suppress=True)

# [8] Display field in xz-plane using matplotlib
X, Z = np.meshgrid(xs, zs)
U, V = Bs[:, :, 0], Bs[:, :, 2]
ax2.streamplot(X, Z, U, V, color=np.log(U ** 2 + V ** 2))

# [9] Display plot
plt.show()
