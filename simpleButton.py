import kivy

from kivy.uix.button import Button
from kivy.app import  App

class MainApp(App):
    def build(self):
        return  Button(text = "Simple button generated in kivy GUI framework")

app=MainApp()
app.run()