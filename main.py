from kivy.config import Config
WIDTH  = int(720 * 0.5)
HEIGHT = int(1400 * 0.5)
Config.set('graphics', 'width', WIDTH)
Config.set('graphics', 'height', HEIGHT)
Config.set('graphics', 'resizable', False)
Config.write()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
class MainApp(App):

    def build(self):
        return Image(source="assets/JDMBG.png")

if __name__ == "__main__":
    MainApp().run()
