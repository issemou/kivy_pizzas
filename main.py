from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior

from http_client import HttpClient
from models import Pizza
from storage_manager import StorageManager


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)

    def on_parent(self, widget, parents):
        pizzas_fdict = StorageManager().load_data("Pizzas")
        if pizzas_fdict:
            self.recycleView.data = pizzas_fdict

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data("Pizzas", pizzas_dict)

    def on_server_error(self, error):
        self.error_str = "Erreur: " + error


Builder.load_file("Pizzaencod.kv")


class PizzaApp(App):
    def build(self):
        return MainWidget()


PizzaApp().run()
