from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    def on_button_click(self):
        self.ids.my_label.text = "Button Clicked!"

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
