# navbar = [{'url': '/', 'label': 'main page'},
#           {'url': 'customer-list', 'label': 'customers'},
#           {'url': 'product-list', 'label': 'products'},
#           {'url': 'order-list', 'label': 'orders'}]


from typing import Dict, Optional
from django.urls import reverse_lazy
from bootstrap_navbar.navbars.base import LazyAttribute
from bootstrap_navbar.navbars.bootstrap4 import (
    NavBar,
    Brand,
    Link,
    Image,
    NavGroup,
    ListItem,
    DropDown,
)
from django.utils.translation import gettext_lazy as _


class MainMenu(NavGroup):
    """Contains the navitems for the site pages."""
    home = ListItem(text=_('main page').title(),
                    href=reverse_lazy("customer:customer-list"))
    customers = ListItem(text=_('customers').title(),
                         href=reverse_lazy("customer:customer-list"))
    products = ListItem(text=_('products').title(),
                        href=reverse_lazy("product-list"))
    orders = ListItem(text=_('orders').title(),
                      href=reverse_lazy("order-list"))
    login = LazyAttribute(method="get_login")
    register = LazyAttribute(method="get_register")

    def get_login(self, context: Dict) -> Optional[ListItem]:
        if context.get('request').user.is_authenticated:
            return ListItem(text="%s (%s)" % (_('logout').title(), context.get('request').user),
                            href=reverse_lazy("logout"))
        else:
            return ListItem(text=_('login').title(),
                            href=reverse_lazy("login"))

    def get_register(self, context: Dict) -> Optional[ListItem]:
        if context.get('request').user.is_authenticated:
            return None
        else:
            return ListItem(text=_('register').title(),
                            href=reverse_lazy("register"))

    class Meta:
        navitems = ("home", "customers", "products", "orders", "login",
                    "register")
        class_list = ["mr-auto"]


# class LeftMenu(NavGroup):
#     """Contains the navitems for the site pages."""

#     user = ListItem(text="No Link")
#     home = ListItem(
#         text="Home", href=Href(url=reverse_lazy("home"), query_params={"field": 100})
#     )
#     blog = ListItem(text="Blog", href=reverse_lazy("blog"))
#     pages = DropDown(
#         text="Pages",
#         children=[
#             Link(text="Home", href=reverse_lazy("example-home")),
#             Link(text="Blog", href=reverse_lazy("example-blog")),
#         ],
#         menu_class_list=["custom-class"],
#         menu_attrs={"data-name": "pages-dropdown"},
#     )
#     documentation = LazyAttribute(method="get_documentation")

#     class Meta:
#         navitems = ("home", "blog", "user", "pages", "documentation")
#         class_list = ["mr-auto"]

#     def get_documentation(self, context: Dict) -> Optional[ListItem]:
#         if not random.choice([True, False]):
#             return None

#         return ListItem(text="Documentation", href=reverse_lazy("blog"))


class MainNavBar(NavBar):
    """A NavBar object consists of nav groups and a brand."""

    main_menu = MainMenu()

    class Meta:
        brand = Brand(
            text="Best & C",
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
