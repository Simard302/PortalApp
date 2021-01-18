from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from data import UserDatabase
from screen_format import build_string
from main import Omnivox

Window.size = (450, 500)


class LoginScreen(Screen):
    pass


class RegistrationScreen(Screen):
    pass

class Main(MDApp):
    def build(self):
        self.database = UserDatabase()

        screen = Builder.load_string(build_string)

        self.theme_cls.primary_palette = "Purple"
        sm = ScreenManager()
        screens = [Screen(name='Title {}'.format(i)) for i in range(4)]
        sm.add_widget(LoginScreen(name='login'))                # 0
        sm.add_widget(RegistrationScreen(name='registration'))  # 1

        self.sm = sm
        self.screens = screens
        return screen

    def doRegistration(self, email, password1, password2):
        if password1 == password2:
            self.database.CreateUser(email, password1)
            print(email)
            print(password1)
        else :
            # Give the client an error here
            print(email)
            print(password1)
            print(password2)


    def verifyLogin(self, email, password):
        print(email)
        print(password)

    def pullOmnivoxAssignments(self, username, password):
        session = Omnivox.startSession(username, password)
        if not session:
            print('Login Failed')
            return
        leaSession = session.startLeaSession()
        leaSession.getAssignments()

    def populateAssignments(self):
        self.pullOmnivoxAssignments(self.OvxUsername, self.OvxPassword)

if __name__ == "__main__":
    Main().run()