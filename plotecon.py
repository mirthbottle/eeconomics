from pylab import *;

x = arange(0,1,0.001)
y1 = 1/(x+1)
y2 = 1/(2-x)

plot(x,y1,x,y2)


frame = gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([])

show()
