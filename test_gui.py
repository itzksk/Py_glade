import sys
import pygtk
import gtk
import gtk.glade

class MyApp:
   wTree = None
   def __init__(self):
	self.gladefile = "test_gui.glade"
	self.wTree = gtk.glade.XML(self.gladefile)
	print "xml created\n"
	self.window = self.wTree.get_widget("MainWindow")
	if (self.window):
		self.window.connect("destroy",gtk.main_quit)

myapp = MyApp()
gtk.main()	
