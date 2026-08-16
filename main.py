from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import webbrowser

class Elevate2026(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=20, spacing=15)
        root.add_widget(Label(text="ELEVATE 2026", font_size="28sp", bold=True))
        root.add_widget(Label(text="RANCHO EL OASIS\nTIJUANA - PILOTO"))
        
        btn = Button(text="DONAR $500 - RANCHO TIJUANA", size_hint_y=None, height=60, background_color=(0, 0.8, 0, 1))
        btn.bind(on_press=lambda x: webbrowser.open("https://mpago.la/1Sgeo4z"))
        root.add_widget(btn)
        
        return root

Elevate2026().run()
