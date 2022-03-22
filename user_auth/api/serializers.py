from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.utils.translation import gettext_lazy as _
from react_django.nav_bar import login_menu_item, register_menu_item
from rest_framework.serializers import CharField, SerializerMethodField
from user_auth.forms import LoginForm, RegisterForm


class UserRegisterSerializer(RegisterSerializer):

	form_fields = RegisterForm().fields

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].label = self.form_fields['username'].label
		self.fields['username'].help_text = self.form_fields['username'].help_text
		self.fields['email'].required = self.form_fields['email'].required
		self.fields['password1'].label = self.form_fields['password1'].label
		self.fields['password1'].help_text = self.form_fields['password1'].help_text
		self.fields['password2'].label = self.form_fields['password2'].label
		self.fields['password2'].help_text = self.form_fields['password2'].help_text

	first_name = CharField(write_only=True,
		required=form_fields['first_name'].required,
		label=form_fields['first_name'].label)
	last_name = CharField(write_only=True,
		required=form_fields['last_name'].required,
		label=form_fields['last_name'].label)

	def get_cleaned_data(self):
		cleaned_data = super().get_cleaned_data()
		cleaned_data['first_name'] = self.validated_data.get('first_name', '')
		cleaned_data['last_name'] = self.validated_data.get('last_name', '')
		return cleaned_data


class UserLoginSerializer(LoginSerializer):

	form_fields = LoginForm().fields

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].label = self.form_fields['username'].label
		self.fields['password'].label = self.form_fields['password'].label
