from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Ellipse, RoundedRectangle


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
            self.count += 1


class DonateButton(FloatLayout):
    pass
