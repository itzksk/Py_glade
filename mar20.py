#!/usr/bin/python
'''  script for test1.glade'''
import pdb
import pygtk
pygtk.require('2.0')
import gtk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
from matplotlib.backends.backend_gtkagg import NavigationToolbar2GTKAgg as NavigationToolbar
import random 
import time
import thread

FALSE = gtk.FALSE
TRUE = gtk.TRUE
MAX_PLOT_LIST = 4
plot_list = ["sine","duck","buck","cuck"]

### main application class
class MyApp:
 #Has to first create all the required gui and wait for events
  cnt_log_thd = 0
  def __init__(self):
	try:
	   builder = gtk.Builder()
	   builder.add_from_file("test1.glade")
	except:
	   print "Failed to load th UI XML file"
	   sys.exit(1)
	
	# To play around with the widgets you need to get their refs
	self.root = builder.get_object("Root")
	self.but_quit = builder.get_object("quit")
	self.im_logo = builder.get_object("racing_logo") #set the logo here or anywhere
	self.vbox_plot = builder.get_object("vbox_plot")
	self.tv_log = builder.get_object("log_display")

	#paint the widgets on your UI
	self.im_logo.set_from_file("logo.jpeg")
	self.tv_log_buffer = self.tv_log.get_buffer()
	self.tv_log.set_editable(FALSE)
	self.tv_log.set_cursor_visible(FALSE)
	#ifile_log = open("log.csv","r") #should tis be opened here or in thread ??
	
	self.plotArea_init()
	builder.connect_signals(self)
	self.root.connect("destroy",lambda x:gtk.main_quit())
## start of event handlers ##
  def on_quit_clicked(self,widget,data = None):
  	print "Exiting App"
	gtk.main_quit()

  def on_showlog_clicked(self,widget,data=None):
	#has to read from the log.csv
	try:
	    if(self.cnt_log_thd == 0):
                thread.start_new_thread(thd_showlog,())
		pdb.set_trace()
                self.cnt_log_thd += 1
	        print "thread created"
            else: print "thread is already created"
	except:
	    print 'Error: unable to start the thread'


	
## End of event handlers ##

## start of class methods ##
  def plotArea_init(self):
  	#for placing and initialising the plot area
	self.fig = Figure(figsize=(5,5), dpi=100)
	self.ax = self.fig.add_subplot(1,1,1)

	self.canvas = FigureCanvas(self.fig)
	self.vbox_plot.pack_start(self.canvas)
	##should add a toolbar ??

	self.combox_plot = gtk.combo_box_new_text()
	self.vbox_plot.pack_end(self.combox_plot,expand=False,fill=True)

	for self.i in range(0,MAX_PLOT_LIST): #preparing the dropdown list
		self.combox_plot.append_text(plot_list[self.i])
	
  def main(self):
	self.root.show_all()
	gtk.main()
## end of class methods ##

## Start of thread bodys ##
def thd_showlog():
        print 'Inside log thread'	
	ifile = open("log.csv")
	for i in range(0,10):
		string = ifile.readline()
		print "Printing "
		myapp1.tv_log_buffer.set_text(string)
		print "string:", string
		time.sleep(0.3)
	ifile.close()

## End of thread bodys ##


if __name__ == "__main__":
	myapp = MyApp()
	myapp1 = myapp
	myapp.main()



	



	


