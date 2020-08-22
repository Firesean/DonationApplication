from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang.builder import Builder

import WindowProperties
import DonateScreen
import MainScreen


# Information is provided in the ovdonate.kv file
class ManageScreens(ScreenManager):
    pass


# Builds the foundation of the application
kv = Builder.load_file("ovdonate.kv")


# Information is provided in the ovdonate.kv file
class OVDonateApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    app = OVDonateApp()
    app.run()
