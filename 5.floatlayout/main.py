import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class Wid_Alfa(FloatLayout):
	None

class MainApp(App):
	title = 'Float Layout'
	def build(self):
		return Wid_Alfa()

if __name__ == '__main__':
	MainApp().run()
