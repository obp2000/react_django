"""
API endpoints that allow current user to be viewed.
"""
from dj_rest_auth.views import UserDetailsView as UserDetailsViewOrig
from react_django.api.consts import get_options

from .consts_data import consts_data


class UserDetailsView(UserDetailsViewOrig):

    def options(self, request, *args, **kwargs):
        return get_options(self, request, consts_data)
