import kivy
kivy.require('1.9.1')

from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.label import Label
from kivy.core.window import Window

class Wid_Alfa(FloatLayout):
	text = 'Nightwish'
	def __init__(self):
		super(Wid_Alfa, self).__init__()
		self.add_widget(Label(text = self.text))

	def increment_text_der(self, *arg):
		self.text += 'd'
		self.canvas.clear()
		self.add_widget(Label(text = self.text))

	def increment_text_izq(self, *arg):
		self.text = 'i' + self.text 
		self.canvas.clear()
		self.add_widget(Label(text = self.text))
	
	def del_scr(self, *arg):
		self.canvas.clear()
		self.text = 'Nightwish'
		self.add_widget(Label(text = self.text))

class MainApp(App):
	title = 'Pruebas App'
	def build(self):
		#	Definimos la pantalla donde alojaremos el texto
		rfl = Wid_Alfa()

		#	Botones
		btn_der = Button(text = '->')
		btn_der.bind(on_press = rfl.increment_text_der)

		btn_del = Button(text = 'del')
		btn_del.bind(on_press = rfl.del_scr)

		btn_izq = Button(text = '<-')
		btn_izq.bind(on_press = rfl.increment_text_izq)

		#	Contenedor de los botones
		layout = BoxLayout(size_hint = (1, None), height = 50)
		layout.add_widget(btn_izq)
		layout.add_widget(btn_del)
		layout.add_widget(btn_der)

		root = BoxLayout(orientation = 'vertical')
		root.add_widget(rfl)
		root.add_widget(layout)
	
		return root

if __name__ == '__main__':
	MainApp().run()
