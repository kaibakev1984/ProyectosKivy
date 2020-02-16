import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 400)

class Mensaje(BoxLayout):
	None

class Box(BoxLayout):
	def __init__(self):
		super(Box, self).__init__()
		self.MENSAJE = Mensaje()

		self.add_widget(self.MENSAJE)


class MainApp(App):
	title = 'Programa de Pruebas'
	def build(self):
		return Box()

if __name__ == '__main__':
	MainApp().run()
