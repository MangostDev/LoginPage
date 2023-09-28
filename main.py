from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class LoginPageApp(App):
    pass

class LoginManager(ScreenManager):
    pass

class Question1Screen(Screen):
    pass

class CorrectScreen(Screen):
    pass

class ErrorScreen(Screen):
    pass

LoginPageApp().run()