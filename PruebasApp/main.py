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
	text_up = ''
	text_down = ''

	def __init__(self):
		super(Wid_Alfa, self).__init__()
		self.add_widget(Label(text = self.text))

	def increment_text_der(self, *arg):
		self.text = ' ' + self.text
		self.canvas.clear()
		aux_txt = self.text_down + self.text + self.text_up
		self.add_widget(Label(text = aux_txt))

	def increment_text_izq(self, *arg):
		if(self.text[0] == ' '):
			self.text = self.text[1:]
			self.canvas.clear()
			aux_txt = self.text_down + self.text + self.text_up
			self.add_widget(Label(text = aux_txt))
	
	def increment_text_down(self, *arg):
		self.text_down += '\n'
		self.canvas.clear()
		aux_txt = self.text_down + self.text + self.text_up
		self.add_widget(Label(text = aux_txt))

	def increment_text_up(self, *arg):
		self.text_up += '\n'
		self.canvas.clear()
		aux_txt = self.text_down + self.text + self.text_up
		self.add_widget(Label(text = aux_txt))

	def del_scr(self, *arg):
		self.canvas.clear()
		self.text = 'Nightwish'
		self.text_up = self.text_down = ''
		aux_txt = aux_txt = self.text_down + self.text + self.text_up
		self.add_widget(Label(text = aux_txt))

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

		btn_down = Button(text = 'abajo')
		btn_down.bind(on_press = rfl.increment_text_down)

		btn_up = Button(text = 'Arriba')
		btn_up.bind(on_press = rfl.increment_text_up)

		#	Contenedor de los botones
		layout = BoxLayout(size_hint = (1, None), height = 50)
		layout.add_widget(btn_izq)
		layout.add_widget(btn_del)
		layout.add_widget(btn_der)

		layout2 = BoxLayout(size_hint = (1, None), height = 50)
		layout2.add_widget(btn_down)

		layout3 = BoxLayout(size_hint = (1, None), height = 50)
		layout3.add_widget(btn_up)

		root = BoxLayout(orientation = 'vertical')
		root.add_widget(rfl)
		root.add_widget(layout3)
		root.add_widget(layout)
		root.add_widget(layout2)

	
		return root

if __name__ == '__main__':
	MainApp().run()
