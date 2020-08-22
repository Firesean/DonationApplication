from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


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
