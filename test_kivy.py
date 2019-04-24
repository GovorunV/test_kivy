from kivy.app import App
from kivy.uix.button import Button #создание кнопки

from kivy.config import Config

Config.set('graphics','resizable','0') #запретить изменение размера окна
Config.set('graphics','width','640') #размер окна
Config.set('graphics','height','480') #размер окна

from kivy.uix.floatlayout import FloatLayout

class MyApp(App):
    def build(self):#создание кнопки
        fl=FloatLayout(size=(300,300))
        return Button(text="Надпись",
                      font_size=40,
                      on_press=self.btn_press,# что происходит после нажатие кнопки
                      background_color = [1,0,0,1],
                      background_normal = "")
    def btn_press(self,instance): #функция которая срабатывает после нажатия
        print("кнопка нажата") #вывод в консоли после нажатия
        instance.text = "Нажата1" #смена надписи кнопки


if __name__ == "__main__":
    MyApp().run()
