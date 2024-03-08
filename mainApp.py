import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WeatherApp(Gtk.Window):
    def __init__(self):
        super().__init__(self, title="MSM Weather App")
        self.set_default_size(400, 300)

        # Create a vertical box container
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Create labels for displaying weather information
        label_location = Gtk.Label(label="Location: City, Country")
        label_temperature = Gtk.Label(label="Temperature: 25°C")
        label_conditions = Gtk.Label(label="Conditions: Sunny")

        # Add labels to the vertical box
        vbox.pack_start(label_location, True, True, 0)
        vbox.pack_start(label_temperature, True, True, 0)
        vbox.pack_start(label_conditions, True, True, 0)

        # Create a refresh button
        refresh_button = Gtk.Button(label="Refresh")
        refresh_button.connect("clicked", self.on_refresh_clicked)

        # Add the refresh button to the vertical box
        vbox.pack_start(refresh_button, True, True, 0)

    def on_refresh_clicked(self, button):
        # Implement the logic to refresh weather data here
        print("Refresh button clicked")




def main():
    win = WeatherApp()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()




if __name__ == '__main__':
    main()
