import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown


class TextWidget(BoxLayout):
    def collect_input(self,file_path):
        text = file_path.text

class InputApp(App):
    title = "Input Application Test"
    def build(self):
        return TextWidget()

if __name__ == '__main__':
    InputApp().run()
