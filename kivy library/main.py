import kivy
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        
        self.text_input = TextInput(
            size_hint_y=None,
            height=32
        )
        
        self.submit_button = Button(
            text="Submit",
            on_press=self.submit_text
        )
        
        self.output_label = Label(
            text="",
            font_size=24,
            size_hint_y=None,
            height=32
        )
        
        self.add_widget(self.text_input)
        self.add_widget(self.submit_button)
        self.add_widget(self.output_label)
        
    def submit_text(self, instance):
        input_text = self.text_input.text
        self.output_label.text = input_text

class UserInputApp(App):
    def build(self):
        return MainLayout()
    
if __name__ == "__main__":
    UserInputApp().run()
