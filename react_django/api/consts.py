from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, validate_integer
from django.db.models import Field
from django.utils.translation import gettext_lazy as _
from react_django.nav_bar import (login_menu_item, logout_menu_item,
                                  menu_items, register_menu_item,
                                  user_menu_item)
from rest_framework import status
from rest_framework.response import Response
from user_auth.forms import RegisterForm


def main_menu(is_authenticated):
    if is_authenticated:
        return menu_items + [user_menu_item, logout_menu_item]
    else:
        return menu_items + [login_menu_item]

def error_messages():
    messages = Field.default_error_messages
    messages.update(RegisterForm.error_messages)
    messages.update({'invalid_email': EmailValidator.message})
    try:
        MinimumLengthValidator().validate('')
    except ValidationError as e:
        messages.update({'short_password': e.messages[0]})
    try:
        validate_integer(0.5)
    except ValidationError as e:
        messages.update({'not_integer': e.messages[0]})
    return messages

def common_consts(is_authenticated):
    return {
            'new': _('new').capitalize(),
            'edit': _('edit').capitalize(),
            'delete': _('delete').capitalize(),
            'add': _('add').capitalize(),
            'successfully': f"{_('successfully').capitalize()}!",
            'yes': _('yes').capitalize(),
            'no': _('no').capitalize(),
            'search': _('search').capitalize(),
            'login': login_menu_item['label'],
            'register': register_menu_item['label'],
            'main_menu': main_menu(is_authenticated),
            'error_messages': error_messages()
        }

def get_options(self, request, consts_data):
    meta = self.metadata_class()
    data = meta.determine_metadata(request, self)
    if data.get('actions', None):
        for method in ['PUT', 'POST']:
            if data['actions'].get(method, None):
                data['actions'][method].update(consts_data)
                data['actions'][method].update({'common_consts':
                    common_consts(request.GET.get('isAuthenticated', None) == 'true')})
    return Response(data=data, status=status.HTTP_200_OK)
