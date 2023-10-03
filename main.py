from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
Builder.load_file("Login.kv")


# class LoginPageApp(App):
#     def build(self):
#         return LoginManager()

class LoginApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass

# class Question1Screen(Screen):
#     def answer_question(self,bool):
#
#         if bool:
#             self.manager.current = "correct"
#         else:
#             self.manager.current = "error"
#
# class Question2Screen(Screen):
#     def answer_question(self,text):
#         if text.lower() == "deep in the heart of texas.":
#             self.manager.current = "correct"
#         else:
#             self.ids.invalid.text = "Invalid guess. \n Try again!"
#             self.ids.invalid.color = "red"
#
#
#
# class CorrectScreen(Screen):
#     def advance(self):
#         self.manager.current = "question2"

class ErrorScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class WelcomeScreen(Screen):
    pass



LoginApp().run()