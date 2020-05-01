import matplotlib.pyplot as plt
import numpy as np
delta = 0.025
xrange = np.arange(-2, 2, delta)
yrange = np.arange(-2, 2, delta)
X, Y = np.meshgrid(xrange,yrange)
# F is one side of the equation, G is the other
F = X**2
G = 1- (5*Y/4 - np.sqrt(np.abs(X)))**2
plt.contour((F - G), [0])
plt.show()