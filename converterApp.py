from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class ConverterApp(MDApp):
    def flip(selfself):
        print("working")

    def convert(self,args):
        val = int(self.input.text,2)
        self. converted.text = str(val)
        self.label.text = "Converted decimal value: "

    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = MDScreen()
        #UI Widgets go here
        self.toolbar = MDToolbar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top":1}
        self.toolbar.right_action_items=[["rotate-3d-variant", lambda  x:self.flip()],["dots-vertical", lambda  x:self.flip()],["account", lambda  x:self.flip()]]
        screen.add_widget(self.toolbar)

        #Logo (transparent png image)
        screen.add_widget(Image(source="RedLogo.png", pos_hint = {"center_x":.5, "center_y":0.65}))

        #User input
        self.input = MDTextField ( halign="center", size_hint=(0.7,1.0),pos_hint = {"center_x":.5, "center_y":0.45}, font_size = 22)
        screen.add_widget(self.input)

        # secondary + primary labels
        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            theme_text_color="Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            theme_text_color="Primary",
            font_style="H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        #Connvert Button
        screen.add_widget(MDFillRoundFlatButton(text="CONVERT",font_size = 17,pos_hint={"center_x": 0.5, "center_y": 0.35}, on_press = self.convert))

        return screen

ConverterApp().run()

#if __name__ == '__main__':
#    ConverterApp().run()