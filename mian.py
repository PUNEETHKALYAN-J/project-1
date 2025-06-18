from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return

    def on_button_click(self):
        # This function will be called when the button is clicked
        label = self.root.ids.my_label
        label.text = "Button Clicked!"

if __name__ == '__main__':
    MyApp().run()
