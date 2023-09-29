from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
Builder.load_file("LoginPage.kv")


class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass

class Question1Screen(Screen):
    def answer_question(self,bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"

class Question2Screen(Screen):
    def answer_question(self,bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"

class CorrectScreen(Screen):
    pass

class ErrorScreen(Screen):
    pass



LoginPageApp().run()