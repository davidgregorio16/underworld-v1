
# 06/23/2022

from database import database
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivymd.uix.list import OneLineListItem
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):
    
    def login(self):
        
        username = self.ids.username.text
        password = self.ids.password.text
        
        if username in database:
            if password == database[username]:
                self.change_screen('MainScreen')
                
            elif password == '':
                dialogs.no_login_input()
                
            else:
                self.incorrect_password()
                
        elif not username in database:
            self.no_account()
            
        else:
            dialogs.no_login_input()
            
    def check_login_data(self):
        
        self.login()
    
    no_login_input_dialog = None
    incorrect_password_dialog = None
    no_account_dialog = None
    patch_notes_dialog = None
    
    def change_screen(self, screen, *args):
        self.manager.current = screen
        
    def no_login_input(self):
        if not self.no_login_input_dialog:
            self.no_login_input_dialog = MDDialog(
                text = 'Please put both of your username and password.',
                radius = [20, 20, 20, 20],
                buttons = [
                    MDFlatButton(
                        text = 'Okay',
                        theme_text_color = 'Custom',
                        text_color = (17/255, 246/255, 237/255, 1),
                        on_release = self.no_login_input_dialog_close
                    )
                ]
            )
        self.no_login_input_dialog.open()
        
    def incorrect_password(self):
        if not self.incorrect_password_dialog:
            self.incorrect_password_dialog = MDDialog(
                text = 'Your password is incorrect.',
                radius = [20, 20, 20, 20],
                buttons = [
                    MDFlatButton(
                        text = 'Okay',
                        theme_text_color = 'Custom',
                        text_color = (17/255, 246/255, 237/255, 1),
                        on_release = self.incorrect_password_dialog_close
                    )
                ]
            )
        self.incorrect_password_dialog.open()
        
    def no_account(self):
        if not self.no_account_dialog:
            self.no_account_dialog = MDDialog(
                text = 'Username does not exist.',
                radius = [20, 20, 20, 20],
                buttons = [
                    MDFlatButton(
                        text = 'Okay',
                        theme_text_color = 'Custom',
                        text_color = (17/255, 246/255, 237/255, 1),
                        on_release = self.no_account_dialog_close
                    )
                ]
            )
        self.no_account_dialog.open()
        
    def patch_notes(self):
        if not self.patch_notes_dialog:
            self.patch_notes_dialog = MDDialog(
                title = 'Patch Notes',
                text = '• Login Screen has been fixed           • No bugs at the moment.                  • Needs improvement.',
                radius = [20, 20, 20, 20],
                buttons = [
                    MDFlatButton(
                        text = 'Okay',
                        theme_text_color = 'Custom',
                        text_color = (17/255, 246/255, 237/255, 1),
                        on_release = self.patch_notes_dialog_close
                    )
                ]
            )
        self.patch_notes_dialog.open()
        
    def no_login_input_dialog_close(self, *args):
        self.no_login_input_dialog.dismiss(force=True)
        
    def incorrect_password_dialog_close(self, *args):
        self.incorrect_password_dialog.dismiss(force=True)
        
    def no_account_dialog_close(self, *args):
        self.no_account_dialog.dismiss(force=True)
        
    def patch_notes_dialog_close(self, *args):
        self.patch_notes_dialog.dismiss(force=True)
        
class MainScreen(Screen):
    pass
    
screen_manager = ScreenManager()
screen_manager.add_widget(LoginScreen(name = 'LoginScreen'))
screen_manager.add_widget(MainScreen(name = 'MainScreen'))

class Item(OneLineListItem):
    divider = None

class DuskkApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.primary_hue = '300'
        return Builder.load_file('underworld.kv')

LabelBase.register(
    name = 'Brusher',
    fn_regular = 'FILE PATH'
)

LabelBase.register(
    name = 'Inter-Bold',
    fn_regular = 'FILE PATH'
)

LabelBase.register(
    name = 'Inter-ExtraLight',
    fn_regular = 'FILE PATH'
)

if __name__ == '__main__':
    DuskkApp().run()
