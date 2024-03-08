import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="Button Clicker 2.0")

        #buttons
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)


    
    def button_clicked(self, widget):
        print("Gametime")




def main():
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()




if __name__ == '__main__':
    main()
