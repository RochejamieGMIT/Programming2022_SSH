# weeklyTask08 - Plot Task.py
#Author: Jamie Roche
#
#
#
#
#Refernece: 
#https://matplotlib.org/stable/tutorials/introductory/pyplot.html#:~:text=matplotlib.,the%20plot%20with%20labels%2C%20etc.
#
#I created a graph that has custom lines, colours, sampled more frequently to have a smother graphh
#Included a title, Legend, Labelled the axis, included a grid, 

import numpy as np
import matplotlib.pyplot as plt


xpoints = np.arange(0.,4.0,0.0001)
# Usingnp.arange instead of np.array as I can set the sampleing frequecny, 
# using a smaller smapling frquency the graphs are smoother. Also, the longer sampling time made the lines not apear to quite reach
# 4 on the x axis

ypoints = xpoints # f(x) = x
gpoints = xpoints**2 # f(x) = x^2
hpoints = xpoints**3 # f(x) = x^3
plt.plot(ypoints,xpoints,"r:",label="straight") # plot y, x, dotted red line, labelled straight

plt.plot(ypoints,gpoints,'b-.', label = "XSquared") # plot y, x^2, dash dot blue line, labelled XSquared
plt.plot(ypoints,hpoints,'g--', label = "XCubed") # plot y, x^3, green dash line, labelled X cubed
plt.title("Week 08 - Plot Task") # give the graph a title
plt.legend() # include the legend
plt.xlabel("X Axis") #Label the axis
plt.ylabel("y Axis")
plt.grid(True) # Give the plot a grid just for customisation 

plt.show()
