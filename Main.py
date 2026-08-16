from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.04, 0.04, 0.04, 1)

class ElevateApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=30)
        title = Label(text='[b]ELEVATE\n2023[/b]', markup=True, font_size='32sp', color=(0,1,0.53,1))
        counter = Label(text='[b]1,289\nSESIONES ACTIVAS[/b]', markup=True, font_size='28sp', color=(0,1,0.53,1))
        btn = Button(text='GENERAR REPORTE', background_color=(0,1,0.53,1), color=(0,0,0,1), font_size='18sp', size_hint=(1,0.25), bold=True)
        self.status = Label(text='72% Completado', color=(0.5,1,1,1))
        layout.add_widget(title)
        layout.add_widget(counter)
        layout.add_widget(self.status)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    ElevateApp().run()
