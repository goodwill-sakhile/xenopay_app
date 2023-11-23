from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
<LoginScreen>:
	name:"login._screen"
	MDBoxLayout:
		orientation:"vertical"
		md_bg_color:[47/float(255), 79/float(255), 79/float(255), 1]
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
			MDLabel:
				text:"Xenopay"
				text_size:self.size
				halign:"center"
				font_size:"20dp"
				valign:"middle"
				color:[1, 1, 1, 1]
		MDBoxLayout:
			md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
			radius:[40, 40, 0, 0]
			FloatLayout:
				size_hint:None, None
				size:self.parent.size
				pos:self.parent.pos
				MDBoxLayout:
					size_hint:None, None
					size:self.parent.size
					orientation:"vertical"
					padding:"5dp", "10dp"
					spacing:5
					Widget:
					MDTextField:
						icon_right:"email-edit"
						hint_text:"email address"
						icon_right_color_normal:"green"
						pos_hint:{"center_x":.5, "center_y":.5}
					MDTextField:
						icon_right:"form-textbox-password"
						hint_text:"password"
						icon_right_color_normal:"green"
						pos_hint:{"center_x":.5, "center_y":.5}
					MDBoxLayout:
						size_hint_y:None
						height:"50dp"
						radius:[40, 40, 40, 40]
						md_bg_color:[0, 154/float(255), 225/float(255), 1]
						MDLabel:
							text:"Login"
							font_size:"18dp"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[1, 1, 1, 1]
					MDBoxLayout:
						size_hint_y:None
						height:"50dp"
						Widget:
						MDIconButton:
							icon:"refresh"
							icon_size:"25dp"
							hint_size:None, None
							size:"50dp", "50dp"
						Widget:
					Widget:
					MDBoxLayout:
						size_hint_y:None
						height:"50dp"
						radius:[40, 40, 40, 40]
						md_bg_color:[0, 0/float(255), 0/float(255), 1]
						MDLabel:
							text:"Sign Up"
							font_size:"18dp"
							text_size:self.size
							halign:"center"
							valign:"middle"
							color:[1, 1, 1, 1]
				MDBoxLayout:
					ScreenManager:
						EmptyScreen:
							name:"empty_screen"
""")
class LoginScreen(MDScreen):
	pass
class EmptyScreen(MDScreen):
	pass
class TestApp(MDApp):
	def build(self):
		root = LoginScreen()
		return root
if __name__ == "__main__":
	TestApp().run()