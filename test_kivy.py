from kivy.app import App
from kivy.uix.button import Button #создание кнопки

from kivy.config import Config #изменение размера окна
from kivy.uix.scatter import Scatter  #дабавление емуляции тоуч
from kivy.uix.floatlayout import FloatLayout
Config.set('graphics','resizable','0') #запретить изменение размера окна
Config.set('graphics','width','640') #размер окна
Config.set('graphics','height','480') #размер окна




class MyApp(App):
    def build(self):
        ss=FloatLayout(size= (350,350))
        ss.add_widget(Button( #создание кнопки
            text="Надпись",
            font_size=40,
            on_press=self.btn_press,# что происходит после нажатие кнопки
            background_color = [1,0,0,1],
            background_normal = "",
            size_hint=(.5, .25),
            pos = (640/2-(640*.5/2), 480/2-(480*.25/2)))) #располождение кнопки по центру)
        sc = Scatter() #дабавление емуляции тоуч
        sc.add_widget(ss) #дабавление емуляции тоуч
        return sc
    def btn_press(self,instance): #функция которая срабатывает после нажатия
        print("кнопка нажата") #вывод в консоли после нажатия
        instance.text = "Нажата1" #смена надписи кнопки


if __name__ == "__main__":
    MyApp().run()
