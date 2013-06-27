from pylab import *;

x = arange(0,0.45,0.001)
y1 = 1/(x+0.8)
y2 = 1/(1.25-x)

plot(x,y1,x,y2)
xlim([-0.05,0.5])
ylim([0.7,1.35]) 

frame = gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.spines['top'].set_color('none')
frame.axes.spines['right'].set_color('none')
frame.axes.get_yaxis().set_ticks([])
frame.axes.set_title("Emissions Market")

ylabel("Price (eg. $/kg)")
xlabel("Quantity (eg. kg)")
text(0.35,1.05, 'Marginal Cost')
text(0.03, 1.25, 'Marginal Benefits')
show()
