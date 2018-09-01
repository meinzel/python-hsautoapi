from kivy.app import App
from kivy.uix.button import Button

class MainApplication(App):
    def build(self):
        return Button(text='Hello World')


if __name__ == '__main__':
    MainApplication().run()
