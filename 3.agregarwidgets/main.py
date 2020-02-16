import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Box01(BoxLayout):
	def __init__(self):
		super(Box01, self).__init__()
		
		#	Instanciamos los Widgets
		self.BR = BoxRed()
		self.BB = BoxBlue()
		self.BG = BoxGreen()
		
		#  Agregamos el espacio en blanco
		self.BR.add_widget(BoxBlue())
		self.BR.add_widget(BoxBlue())
	
		self.BG.add_widget(self.BB)
		self.BG.add_widget(BoxBlue())

		self.add_widget(self.BR)
		self.add_widget(self.BG)

class BoxRed(BoxLayout):
	None

class BoxGreen(BoxLayout):
	None

class BoxBlue(BoxLayout):
	None

class MainApp(App):
	title = 'BoxLayout Método 1'
	def build(self):
		return Box01()

if __name__ == '__main__':
	MainApp().run()
