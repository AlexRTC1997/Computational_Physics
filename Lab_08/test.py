# https://resteche.github.io/REsteche_blog/chaos%20theory/butterfly%20effect/python%20animation/2021/10/20/Lorenz_animation.html

import numpy as np
import matplotlib.pyplot as plt


def lorenz(x, y, z, sigma=10, rho=28, beta=2.667):
    x_dot = sigma*(y - x)
    y_dot = rho*x - y - x*z
    z_dot = x*y - beta*z
    return x_dot, y_dot, z_dot

# == PART 1 ==


dt = 0.01
num_steps = 2000

xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)


xs[0], ys[0], zs[0] = (0., 1., 1.05)

for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


ax = plt.figure().add_subplot(projection='3d')


ax.scatter(xs, ys, zs, s=2, c=plt.cm.jet(zs/max(zs)))
ax.plot(xs, ys, zs, color='grey')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()

# == PART 2 ==

# dt = 0.01
# num_steps = 10000

# xs = np.empty(num_steps + 1)
# ys = np.empty(num_steps + 1)
# zs = np.empty(num_steps + 1)


# xs[0], ys[0], zs[0] = (0., 1., 1.05)

# for i in range(num_steps):
#     x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
#     xs[i + 1] = xs[i] + (x_dot * dt)
#     ys[i + 1] = ys[i] + (y_dot * dt)
#     zs[i + 1] = zs[i] + (z_dot * dt)

# fig, ax = plt.subplots(1, 3, sharex=False, sharey=False, figsize=(17, 6))

# # plot the x values vs the y values
# ax[0].plot(xs, ys, color='r', alpha=0.7, linewidth=0.3)
# ax[0].set_title('x-y phase plane')

# # plot the x values vs the z values
# ax[1].plot(xs, zs, color='m', alpha=0.7, linewidth=0.3)
# ax[1].set_title('x-z phase plane')

# # plot the y values vs the z values
# ax[2].plot(ys, zs, color='b', alpha=0.7, linewidth=0.3)
# ax[2].set_title('y-z phase plane')

# plt.show()
