from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

red=[1,0,0]
green=[0,1,0]
blue=[0,0,1]
yellow=[1,1,0]
aqua=[0,1,1]
pink=[1,0,1]
white=[1,1,1]

class MainApp(App):
    def build(self):
        label = Label(text='ТЕСТ',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        img = Image(source='C:/Users/Дом/Desktop/Photo/Dante.png',
                    size_hint=(.5, .5),
                    pos_hint={'center_x': .4, 'center_y': .5})
        layout = BoxLayout()
        colors = [red, green, blue, yellow, aqua, pink, white]
        for i in range(5):
            button = Button(text="Press #%s" % (i+1),
                            background_color=random.choice(colors),
                            color=random.choice(colors)
                            )
            layout.add_widget(button)
        return layout

MainApp().run()