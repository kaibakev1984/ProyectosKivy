#	Vamos a crear un AnchorLayout Movil

import kivy
kivy.require('1.9.1')

from kivy.app import App 
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button 

class Wid_Alfa(AnchorLayout):
	def __init__(self):
		super(Wid_Alfa, self).__init__()
		anchor_x = 'right'
		anchor_y = 'top'

	def move_left(self, *arg):
		self.anchor_x = 'left'
	
	def move_right(self, *arg):
		self.anchor_x = 'right'

	def move_top(self, *arg):
		self.anchor_y = 'top'

	def move_bottom(self, *arg):
		self.anchor_y = 'bottom'

	def reset_move(self, *arg):
		self.anchor_x = 'center'
		self.anchor_y = 'center'

class MainApp(App):
	title = 'Anchor Layout'
	def build(self):
		wid = Wid_Alfa()


		btn_right = Button(text = 'right')
		btn_right.bind(on_press = wid.move_right)

		btn_left = Button(text = 'left')
		btn_left.bind(on_press = wid.move_left)
		
		btn_top = Button(text = 'top')
		btn_top.bind(on_press = wid.move_top)

		btn_bottom = Button(text = 'bottom')
		btn_bottom.bind(on_press = wid.move_bottom)

		btn_reset = Button(text = 'reset')
		btn_reset.bind(on_press = wid.reset_move)

		layout_1 = BoxLayout(size_hint = (1, None), height = 50)
		layout_1.add_widget(btn_top)

		layout_2 = BoxLayout(size_hint = (1, None), height = 50)
		layout_2.add_widget(btn_left)
		layout_2.add_widget(btn_reset)
		layout_2.add_widget(btn_right)

		layout_3 = BoxLayout(size_hint = (1, None), height = 50)
		layout_3.add_widget(btn_bottom)

		root_layout = BoxLayout(orientation = 'vertical', size_hint = (1, None), height = 50)
		root_layout.add_widget(layout_1)
		root_layout.add_widget(layout_2)
		root_layout.add_widget(layout_3)

		root = BoxLayout(orientation = 'vertical')
		root.add_widget(wid)
		root.add_widget(root_layout)

		return root

if __name__ == '__main__':
	MainApp().run()