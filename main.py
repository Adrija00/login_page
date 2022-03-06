from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import json
from datetime import datetime 
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('design.kv')

class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.transition.direction="down"
        self.manager.current="login_screen"
        
    def login(self,uname,pword):
        self.manager.transition.direction="right"
        


class LoginScreen(Screen):
    def Sign_up(self):
        self.manager.current="signup_screen"

    def login(self,uname,pword):
        
        with open("user.json") as file:
            users=json.load(file)
            if uname in users and users[uname]['password'] == pword :
                self.manager.current="loginscreensuccess" # to show the screen made in kv
            else:
                self.ids.error.text='Wrong Username or password'
class SignUpScreenSuccess(Screen):
    def gotologin(self):
        self.manager.transition.direction='up'
        self.manager.current="login_screen"
        
class MainApp(App):
    def build(self):
        return RootWidget()

class ImageButton(ButtonBehavior,HoverBehavior,Image):
    pass

class SignUpScreen(Screen):
    def Add_user(self,uname,pwd):
        with open("user.json") as file:
            user=json.load(file)
            user[uname]={'username':uname,'password':pwd,
            'created':datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
            print(user)
            file.close
            file=open("user.json","w")
            json.dump(user,file)
            file.close
            self.manager.current="signup_screen_success"
class RootWidget(ScreenManager):
    pass

if __name__=="__main__":
    MainApp().run()