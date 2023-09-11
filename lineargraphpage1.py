import numpy as np                 
import matplotlib.pyplot as plt    


#make two columns of graphs
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(14,8))

#set up size of graphs
axisdim = 9

#set up axes
ax1.set(xlim=(-axisdim, axisdim), ylim=(-axisdim, axisdim), aspect='equal')
ax2.set(xlim=(-axisdim, axisdim), ylim=(-axisdim, axisdim), aspect='equal')
ax1.spines['bottom'].set_position('zero')
ax1.spines['left'].set_position('zero')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['bottom'].set_position('zero')
ax2.spines['left'].set_position('zero')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
ax1.set_xlabel('x', size=14, labelpad=-24, x=1.03) 
ax1.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)
ax2.set_xlabel('x', size=14, labelpad=-24, x=1.03)
ax2.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

#set up ticks
ax1.set_xticks([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10])
ax1.set_yticks([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10])
ax2.set_xticks([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10])
ax2.set_yticks([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10])

#put grid behind graphs
ax2.grid(True)
ax1.grid(True)

#set up arrows
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax1.plot((1), (0), marker='>', transform=ax1.get_yaxis_transform(), **arrow_fmt)
ax1.plot((0), (1), marker='^', transform=ax1.get_xaxis_transform(), **arrow_fmt)
ax2.plot((1), (0), marker='>', transform=ax2.get_yaxis_transform(), **arrow_fmt)
ax2.plot((0), (1), marker='^', transform=ax2.get_xaxis_transform(), **arrow_fmt)

    


# Enter x and y coordinates of points and colors
x1 = [-3, 1]
y1 = [-3, 1]
ax1.scatter(x1, y1,c='k')
ax2.scatter(1, 4,c='b')
ax2.scatter(1, 0,c='m')
ax2.scatter(1, 1,c='k')

#set up lines putting label here used in legend
x =np.linspace(-axisdim,axisdim)
ax1.plot(x, x,c='k',lw=1.5, label = 'y = x')
ax2.plot(x, x+3,c='b',lw=1.5, label="y = x + 3")
ax2.plot(x, x,c='k',lw=1.5, label='y = x')
ax2.plot(x, x-1,c='m',lw=1.5, label="y = x - 1")

#set up legend
ax1.legend(loc="lower right")
ax2.legend(loc="lower right")

#set up text
ax1.text(-9,11.5,"This is a graph of the line y = x.\n\nAll of the points on this line have the same x-coordinate and y-coordinate;\
                 \nfor example, (1,1) and (-3,-3).")
ax2.text(-9,11.5,"If we move the line up or down,\nthe x- and y-coordinates of the points are no longer the same.\
                 \n\nThis means that the equation of the new line cannot be y = x.")
ax2.text(-9,-11,"The equation changes by " + r"$\bf{"+ 'adding' +"}$" +" or "+ r"$\bf{"+ 'subtracting' +"}$" + " a number from x.")

#display
#plt.savefig('linearintro1.png',bbox_inches='tight')
plt.show()

