from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
Builder.load_file("Login.kv")

users = {'testlogin': '12369'}


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
    def check(self, username, password):
        if username in users:
            if password == users[username]:
                self.manager.current = "welcome"
            else:
                self.ids.error.text = "Invalid Credentials"
                self.ids.error.color = "red"
        else:
            self.ids.error.text = "Invalid Credentials"
            self.ids.error.color = "red"

    def signup(self):
        self.manager.current = "register"

class RegisterScreen(Screen):
    def register(self, username, password, reenter):
        if username not in users:
            if password == reenter:
                capital = self.contains_character("ABCDEFGHIJKLMNOPQRSTUVWXYZ", password)
                lowercase = self.contains_character("abcdefghijklmnopqrstuvwxyz", password)
                special = self.contains_character("~!@#$%^&*()_-+={}[]|/?:;,.<>", password)
                number = self.contains_character("1234567890", password)
                if capital and lowercase and special and number:
                    if len(password) >= 8:
                        self.manager.current = "login"
                        users[username] = password
                    else:
                        self.ids.error.text = "Password must be at least 8 characters in length."
                        self.ids.error.color = 'red'
                else:
                    self.ids.error.text = "Make sure your password contains each of the required characters."
                    self.ids.error.color = "red"
            else:
                self.ids.error.text = "Passwords must match."
                self.ids.error.color = "red"
        else:
            self.ids.error.text = "Username taken."
            self.ids.error.color = "red"



    def contains_character(self, characters, string):
        for character in characters:
            if character in string:
                return True
                break
            else:
                continue
        return False


class WelcomeScreen(Screen):
    pass


LoginApp().run()