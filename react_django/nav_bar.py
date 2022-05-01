from typing import Dict, Optional

from bootstrap_navbar.navbars.base import LazyAttribute
from bootstrap_navbar.navbars.bootstrap4 import (Brand, DropDown, Image, Link,
                                                 ListItem, NavBar, NavGroup)
from customer.models import Customer
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from order.models import Order
from product.models import Product

menu_items = [
        {
            'path': reverse_lazy('index'),
            'label': _('main').capitalize()
        },
        {
            'path': reverse_lazy("customer:list"),
            'label': Customer._meta.verbose_name_plural.capitalize()
        },
        {
            'path': reverse_lazy("product:list"),
            'label': Product._meta.verbose_name_plural.capitalize()
        },
        {
            'path': reverse_lazy("order:list"),
            'label': Order._meta.verbose_name_plural.capitalize()
        },
    ]

user_menu_item = {
            'path': reverse_lazy("user_detail"),
            'label': get_user_model()._meta.verbose_name.capitalize()
    }

login_menu_item = {
            'path': reverse_lazy("login"),
            'label': _('login').title()
    }

register_menu_item = {
            'path': reverse_lazy("register"),
            'label': _('register').title()
    }

logout_menu_item = {
            'path': reverse_lazy("logout"),
            'label': _('logout').title()
    }

brand_text = "Best & C"


class MainMenu(NavGroup):
    """Contains the navitems for the site pages."""
    home = ListItem(text=menu_items[0]['label'], href=menu_items[0]['path'])
    customers = ListItem(text=menu_items[1]['label'], href=menu_items[1]['path'])
    products = ListItem(text=menu_items[2]['label'], href=menu_items[2]['path'])
    orders = ListItem(text=menu_items[3]['label'], href=menu_items[3]['path'])
    user = LazyAttribute(method="get_user")
    login = LazyAttribute(method="get_login")
    register = LazyAttribute(method="get_register")

    def get_user(self, context: Dict) -> Optional[ListItem]:
        if context.get('request').user.is_authenticated:
            return ListItem(text=user_menu_item['label'],
                            href=user_menu_item['path'])
        else:
            return None

    def get_login(self, context: Dict) -> Optional[ListItem]:
        user = context.get('request').user
        if user.is_authenticated:
            return ListItem(text=f"{logout_menu_item['label']} ({user})",
                            href=logout_menu_item['path'])
        else:
            return ListItem(text=login_menu_item['label'],
                            href=login_menu_item['path'])

    def get_register(self, context: Dict) -> Optional[ListItem]:
        if context.get('request').user.is_authenticated:
            return None
        else:
            return ListItem(text=register_menu_item['label'],
                            href=register_menu_item['path'])

    class Meta:
        navitems = ("home", "customers", "products", "orders", "user", "login",
                    "register")
        class_list = ["mr-auto"]


class MainNavBar(NavBar):
    """A NavBar object consists of nav groups and a brand."""
    main_menu = MainMenu()

    class Meta:
        brand = Brand(
            text=brand_text,
            href="/",
            # attrs={"target": "_"},
            image=Image(
                src=(
                    "https://getbootstrap.com/docs/4.0/"
                    "assets/brand/bootstrap-solid.svg"
                ),
                attrs={"width": 30, "height": 30},
                class_list=[
                    "d-inline-block",
                    "align-top",
                    "border",
                    "border-white",
                    "rounded",
                ],
            ),
        )
        attrs = {"style": "background-color: #563d82;"}
        navgroups = ("main_menu",)
        class_list = ["navbar-dark"]
