from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.utils.translation import gettext_lazy as _
from react_django.nav_bar import login_menu_item, register_menu_item
from rest_framework.serializers import CharField, SerializerMethodField
from user_auth.forms import LoginForm, RegisterForm


class UserRegisterSerializer(RegisterSerializer):

	def get_parent_field(field_name):
		return RegisterSerializer().fields[field_name]

	def get_parent_username_field():
		return get_parent_field('username')

	def get_parent_email_field():
		return get_parent_field('email')

	def get_parent_password1_field():
		return get_parent_field('password1')

	def get_parent_password2_field():
		return get_parent_field('password2')

	def help_text(field_name):
		return getattr(RegisterForm().fields[field_name], 'help_text', None)

	def label(field_name):
		return getattr(RegisterForm().fields[field_name], 'label', None)

	def required(field_name):
		return getattr(RegisterForm().fields[field_name], 'required', None)

	username = CharField(source='get_parent_username_field',
		help_text=help_text('username'), label=label('username'))
	email = CharField(source='get_parent_email_field',
		label=label('email'))
	first_name = CharField(write_only=True, required=required('first_name'),
		label=label('first_name'))
	last_name = CharField(write_only=True, required=required('last_name'),
		label=label('last_name'))
	password1 = CharField(source='get_parent_password1_field',
		help_text=help_text('password1'), label=label('password1'))
	password2 = CharField(source='get_parent_password2_field',
		help_text=help_text('password2'), label=label('password2'))

	def get_cleaned_data(self):
		cleaned_data = super().get_cleaned_data()
		cleaned_data['first_name'] = self.validated_data.get('first_name', '')
		cleaned_data['last_name'] = self.validated_data.get('last_name', '')
		return cleaned_data


class UserLoginSerializer(LoginSerializer):

	def get_parent_field(field_name):
		return LoginSerializer().fields[field_name]

	def get_parent_username_field():
		return get_parent_field('username')

	def get_parent_password_field():
		return get_parent_field('password')

	def label(field_name):
		return getattr(LoginForm().fields[field_name], 'label', None)

	username = CharField(source='get_parent_username_field',
		label=label('username'))
	password = CharField(source='get_parent_password_field',
		label=label('password'))

	def to_internal_value(self, data):
		return data
