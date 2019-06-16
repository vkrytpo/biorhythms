#import all modules
from datetime import date
import matplotlib.dates
from pylab import *
from numpy import array,sin,pi


#function for input date
def get_date():
    d= input("please enter date (DD/MMP/YYYY ):")
    format_d=[]
    try:
        for x in d.split("/"):
            format_d.append(int(x))
        return format_d[0],format_d[1],format_d[2]
    except:
        print("invalid input ,try again !")
        get_date()

		
#getting date of birth.
print("enter your date of birth:")
dd,mm,yy = get_date()


#getting target date.
print("enter target date: ")
dd1,mm1,yy1 = get_date()

#converting dates to ordinal.
t0 = date(yy,mm,dd).toordinal()
t1 = date(yy1,mm1,dd1).toordinal()

#creating range of 30 days.
t = array(range(t1-3,t1+31)) 


#function for day of week
def findday(d, m, y): 
    t = [ 0, 3, 2, 5, 0, 3, 
          5, 1, 4, 6, 2, 4 ] 
    y -= m < 3
    return (( y + int(y / 4) - int(y / 100) 
             + int(y / 400) + t[m - 1] + d) % 7) 

#creating sine curves and storing into y.
a=[]
a.append(sin(2*pi*(t-t0)/23)) #physical
a.append(sin(2*pi*(t-t0)/28)) #emotional
a.append(sin(2*pi*(t-t0)/33)) #Intellectual
y=(a[0],a[1],a[2])

#making labels for graph.
label = []
for p in t:
 label.append(date.fromordinal(p))
 
#initializing matplotlib figure
fig = figure(figsize=(14,7)) 
ax = fig.gca()
plot(label,y[0], color="r", linewidth=4, alpha=.7)
plot(label,y[1], color="b", linewidth=4, alpha=.7)
plot(label,y[2], color="g", linewidth=4, alpha=.7)


#function to check wheather a value is positive or negative
def p_or_n(q):
	if q>=0: return 1
	return 0

for n in range(len(t)-1):
	#print ("%s %3.1f %3.1f %3.1f" % (label[n], f(y[0][n]), f(y[1][n]), f(y[2][n])))
	if ( p_or_n(y[0][n])!=p_or_n(y[0][n+1]) or
	     p_or_n(y[1][n])!=p_or_n(y[1][n+1]) or
	     p_or_n(y[2][n])!=p_or_n(y[2][n+1]) ):
		print (label[n], "***")

#adding a legend
legend(['Physical', 'Emotional', 'Intellectual'])    

ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d/%b'))
axhline(0, color="black", linewidth=1.4)
grid(True, linestyle="-", alpha=.3)
xlim((t[0],t[-1]))
title("%02u.%02u.%04u (Alter: %u Target Date %02u.%02u.%04u)" % (dd,mm,yy, t1-t0, dd1, mm1, yy1))

#saving fig in jpg
fn = "%04u-%02u-%02u.jpg" % (yy,mm,dd)
savefig(fn)

show() #Showing figure             


