from kivy.app import App
from kivy.uix.button import Button
from hsautoapi.apicalls.debugdrawingapicalls import printresolution

# from win32api import GetSystemMetrics

# def printresolution():
#     width = GetSystemMetrics (0)
#     height = GetSystemMetrics (1)
#     print ('Screen resolution = %dx%d' % (width, height))

class MyButton(Button):
    def on_press(self):
        printresolution()

def callback(instance):
    print('The button <%s> is being pressed' % instance.text)

class MainApplication(App):
    def build(self):
        #btn1 = Button(text='Hello world 1')
        #btn1.bind(on_press=callback)
        #return btn1
        return MyButton(text="hello world")


if __name__ == '__main__':
    MainApplication().run()
