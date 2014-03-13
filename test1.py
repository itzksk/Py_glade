''' Application script for test1.glade'''

import pygtk
pygtk.require('2.0')
import gtk

class MyApp:
   def __init__(self):
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
	
	#text view for log diaply,read-only
	self.tv_log = builder.get_object("log_display")
	self.text_buffer = self.tv_log.get_buffer() #get the buffer of text view widget
	self.tv_log.set_editable(gtk.FALSE)
	self.tv_log.set_cursor_visible(gtk.FALSE)
	self.ifile = open("log.csv","r")
	

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


   def main(self):
   	self.root.show_all() # shows all widgets inside the 'root' container
   	gtk.main()


if __name__ == "__main__":
   myapp = MyApp()
   myapp.main()

