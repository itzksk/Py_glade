''' Application script for test1.glade'''

import pygtk
pygtk.require('2.0')
import gtk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
import matplotlib.animation as animation

MAX_PLOT_LIST = 4
plot_list = ["sine","line","blah","yuck"]
class MyApp:
   def __init__(self):
	self.i=1
	try:
	   builder = gtk.Builder()  
	   builder.add_from_file("test1.glade")
	except:
	   print"Failed to load the UI XML file"
	   sys.exit(1)

	#getting the references to widgets
	self.root = builder.get_object("Root")
	self.but_quit = builder.get_object("quit")
	self.im_logo = builder.get_object("racing_logo")
	self.im_logo.set_from_file("logo.jpeg")
	self.vbox_plot = builder.get_object("vbox_plot")
	#text view for log diaply,read-only
	self.tv_log = builder.get_object("log_display")
	self.text_buffer = self.tv_log.get_buffer() #get the buffer of text view widget
	self.tv_log.set_editable(gtk.FALSE)
	self.tv_log.set_cursor_visible(gtk.FALSE)
	self.ifile = open("log.csv","r")
	
	self.plot_init()

	#connecting signal
	builder.connect_signals(self)
   def on_quit_clicked(self,widget,data = None):
	print"Exiting app"
	self.ifile.close()
	gtk.main_quit()

   def on_showlog_clicked(self,widget,data = None):
   	#has to read from log file and show contents in text box
#	self.ifile = open("log.csv","r")
	self.string = self.ifile.readline()
	self.text_buffer.set_text(self.string)
#	self.ifile.close()
   def on_start_plot_clicked(self,widget,data=None):
	print"started plotting"

   # below are methods of this class
   def plot_init(self):
	self.fig = Figure(figsize=(10,10), dpi=100)
	self.ax = self.fig.add_subplot(1,1,1)
	self.ax.plot([1,2,3,4])
	self.canvas = FigureCanvas(self.fig)
	self.vbox_plot.pack_start(self.canvas)
	
	self.combox_plot = gtk.combo_box_new_text()
	self.vbox_plot.pack_end(self.combox_plot,expand=False,fill=True)
	
	for self.i in range(0,MAX_PLOT_LIST): #preparing the dropdown list
		self.combox_plot.append_text(plot_list[self.i]) 	
	
	# for animation plot
	self.fig1 = plt.figure()
#	self.vbox_plot.add(self.fig1)
	self.data = np.random.rand(2, 25)
	self.l, = plt.plot([], [], 'r-')
	plt.xlim(0, 1)
	plt.ylim(0, 1)
	plt.xlabel('x')
	plt.title('test')
	self.line_ani = animation.FuncAnimation(self.fig1, self.update_line, 25, fargs=(self.data, self.l),
	    interval=50, blit=True)
	plt.show()
   def update_line(self,num,data,line):
	line.set_data(data[...,:num])
	return line,

	
		
   def main(self):
   	self.root.show_all() # shows all widgets inside the 'root' container
   	gtk.main()


if __name__ == "__main__":
   myapp = MyApp()
   myapp.main()

