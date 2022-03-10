# leaerning  matplotlib

from turtle import color
import numpy as np
import matplotlib.pyplot as plt


xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints
plt.plot(xpoints,xpoints,label="straight",color="blue")

plt.plot(xpoints,ypoints, label = "Xsquared")
plt.legend()

randompoints = np.random.randint(1,1000,100)
plt.scatter(xpoints,randompoints,label="random")

plt.show()


