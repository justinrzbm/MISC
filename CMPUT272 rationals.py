# Justin Rozeboom

# This graph visualizes the proof that the set of rational numbers is countable.

from matplotlib import pyplot as plt
import numpy as np
import math
size = 10
x_array = np.arange(-size, size+1)
ys = [np.full(np.size(x_array), i) for i in range(size+1)] # creates 


# draw lines
clr = 'red'
lw = 1
for i in range(size+2):
    if i==0:
        plt.plot((0,0,1,1,2),(0,1,1,0,0) , color=clr, linewidth=lw)
    else:
        if i%2 == 0:
            plt.plot((i, i, i-(2*i-1), i-(2*i-1), i-(2*i-1)-1), (0, i, i, 0, 0), color=clr, linewidth=lw)
        else:
            plt.plot((1-i, 1-i, 1-i+(2*i-1), 1-i+(2*i-1), 1-i+(2*i-1)+1), (0, i, i, 0, 0), color=clr, linewidth=lw)

# make dots, starting from bottom left, in rows from bottom to top
for y_top in range(1, size+1):
    for y in range(1, y_top): # start at row 1 to avoid dividing x/0
        for x_top in range(-size, size+1):
            for x in range(-size, size+1):
                if x_top/y_top == x/y: # move the point off plot
                    x_array[x_top+size] = 0
                    ys[y_top][x_top+size] = -5

    plt.plot(x_array, ys[y_top], 'o', color="blue")
    x_array = np.arange(-size, size+1) # reset x

plt.plot(0, 0, 'o', color="black") # plot 0,0



plt.axis([-size,size,-1,size])
plt.grid(True)
plt.title("Rationals of x/y")
plt.xticks(np.arange(-size, size+1, step=1))
plt.yticks(np.arange(0, size+1, step=1))
plt.show()