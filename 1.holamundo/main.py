import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 400)

class Box01(BoxLayout):
	None

class MainApp(App):
	title = 'Hola Mundo'
	def build(self):
		return Box01()

if __name__ == '__main__':
	MainApp().run()
