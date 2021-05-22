from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.serializers import (ModelSerializer, Serializer,
                                        CharField, ValidationError)

User._meta.get_field('email')._unique = True


class UserSerializer(ModelSerializer):
    """
    User serializer.
    """
    class Meta:
        """
        Set User serializer.
        """
        model = User
        fields = (
            'id',
            'username',
            'email'
        )


class RegisterSerializer(ModelSerializer):
    """
    User register serializer.
    """
    class Meta:
        """
        Set User register serializer.
        """
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class LoginSerializer(Serializer):
    """
    User login serializer.
    """
    username = CharField()
    # email = CharField()
    password = CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise ValidationError("Incorrect Credentials")
