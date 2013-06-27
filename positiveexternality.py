from pylab import *;

x = arange(0,0.45,0.001)
y1 = 0.7*x+.82
y2 = 1.25-x
y3 = 1.4*x - 1/(1.25-x) +1.6

plot(x,y1,x,y2,x,y3)
xlim([-0.05,0.5])
ylim([0.7,1.35]) 

frame = gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.spines['top'].set_color('none')
frame.axes.spines['right'].set_color('none')
frame.axes.get_yaxis().set_ticks([])
frame.axes.set_title("Low Carbon Fuel Market")

ylabel("Price")
xlabel("Quantity")
text(0.35,1.05, 'MC to Firms')
text(0.03, 1.25, 'MB to Consumers/Society')
text(0.03,0.8, 'MC to Society')
show()
