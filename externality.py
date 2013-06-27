from pylab import *;

x = arange(0,0.45,0.001)
y1 = 1.25-x
y2 = 0.7*x+.82
y3 = 1/(1.25-x)+0.05

plot(x,y1,x,y2,x,y3)
xlim([-0.05,0.5])
ylim([0.7,1.35]) 

frame = gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.spines['top'].set_color('none')
frame.axes.spines['right'].set_color('none')
frame.axes.get_yaxis().set_ticks([])
frame.axes.set_title("Transportation Fuel Market")

ylabel("Price")
xlabel("Quantity")
text(0.27,1.25, 'MC to Society')
text(0.3, 1, "MC to Firms")
text(0.03, 1.24, 'MB to Consumers')
show()
