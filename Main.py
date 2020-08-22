import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import RoundedRectangle, Ellipse, Canvas
kivy.require("1.11.1")

Window.clearcolor = (1, 1, 1, 1)  # Sets background of window to white
# Window.fullscreen = True  # Usage of fullscreen is for mobile phones
# Portrait
Window.size = (316, 600)  # Approximate size of my phone
# Landscape
# Window.size = (600, 316)
# Landscape
# Window.size = (960, 650)  # Approximate size of my iPad
# Portrait
# Window.size = (650, 960)


class DonateButton(FloatLayout):
    pass


# Information is provided in the ovdonate.kv file
class DonateScreen(Screen):
    count = 0
    costs = [10, 25, 50, 75, 100, 250, 500]
    descriptions = {"EN": ["Our Supplies!",
                           "Our Equipment!",
                           "Our Dreams!",
                           "Our Experiences!",
                           "Our Programs!",
                           "Our Interests!",
                           "Our Technology!"],
                    "ES": ["Nuestros Suministros",
                           "Nuestro equipo",
                           "Nuestros suenos",
                           "Nuestras Experiencias",
                           "Nuestras Programas",
                           "Nuestros intereses",
                           "Nuestra tecnologia"]}

    def prep_screen(self):
        lang = self.parent.get_screen("main").langSwitchObj.text
        ch = self.children
        spacer = .15
        offset = .025
        #  Children of screen - ch
        for obj in ch:
            if type(obj).__name__ == DonateButton.__name__:
                # Offset + Set Position
                # Spaces to move over + Total Spaced moved
                new_pos = self.count * spacer + offset
                new_pos = {"y": new_pos}
                kids = obj.children
                # Description
                kids[0].color = 0, 0, 0, 1
                kids[0].text = self.descriptions[lang][len(self.descriptions[lang]) - self.count - 1]
                kids[0].pos_hint = new_pos

                # Cost
                kids[1].color = 0, 0, 0, 1
                kids[1].text = f"${self.costs[len(self.costs) - self.count - 1]}"
                kids[1].pos_hint = new_pos

                #  Sets the image in the ellipse
                sources = "images/{0}Dollar.jpg".format(self.costs[len(self.costs) - self.count - 1])
                screen = [child.children for child in self.canvas.children]
                for widget in screen:
                    for cnv_obj in widget:

                        if type(cnv_obj).__name__ in [Ellipse.__name__, RoundedRectangle.__name__]:
                            cnv_obj.pos = cnv_obj.pos[0], cnv_obj.pos[1] + 200
                            # cvs.get_group("image")[0].source = sources
            self.canvas.clear()
            self.canvas.draw()

            self.count += 1


# Information is provided in the ovdonate.kv file
class MainScreen(Screen):
    missionObj = ObjectProperty(None)
    headingObj = ObjectProperty(None)
    langSwitchObj = ObjectProperty(None)
    donateObj = ObjectProperty(None)
    copyrightObj = ObjectProperty(None)
    donateVideoObj = ObjectProperty(None)

            # English Translations
    langs = {"EN": ["Give the Gift\nof Opportunity",  # New line for better display on mobile
                    """For over 65 years, Opportunity Village has been dedicated to improving the lives of individuals with disabilities and assisting them on their journey of becoming the absolute best version of themselves.""",
                    "GIFT US TODAY",
                    "Copyright " + u"\u00A9 " + " 2020, Opportunity Village, Inc. All rights reserved"],
             # Spanish Translations
             "ES": ["Regala la \noportunidad",  # New line for better display on mobile
                    """Durante mas de 65 anos, Opportunity Village se ha dedicado a mejorar las vidas de las personas con discapacidades y a ayudarlas en su viaje para convertirse en la mejor version de si mismos""",
                    "REGALANOS HOY",
                    "Copyright " + u"\u00A9 " + " 2020, Opportunity Village, Inc. Todos los derechos reservados"]}

    def switch_lang_main(self):
        changeable_widgets = [self.headingObj, self.missionObj, self.donateObj, self.copyrightObj]
        lang = self.langSwitchObj.text
        for obj in changeable_widgets:
            i = changeable_widgets.index(obj)
            obj.text = self.langs[lang][i]


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
