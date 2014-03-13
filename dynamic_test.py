import random
import matplotlib.pyplot as plt
import gtk 
import time
items = [1,2,3,4,5,6,7,8,9]
def plot():
	print 'plotting'	
	line, = plt.plot(items)


	print "updating"
	ax = plt.gca()
	for i in range(0,100):
		random.shuffle(items)
		#ax.plot(items)
		plt.setp(line,ydata=items)
		plt.draw()
		time.sleep(0.5)


plt.ion()
plot()
gtk.main()


