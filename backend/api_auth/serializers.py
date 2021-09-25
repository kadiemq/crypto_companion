from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

from api_auth.models import NewUser


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=NewUser.objects.all())])
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=NewUser.objects.all())])
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = NewUser
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        write_only_fields = ('password')

    def validate(self, args):
        first_name = args.get('first_name', )
        last_name = args.get('last_name', )
        email = args.get('email', )
        username = args.get('username', )
        password = args.get('password', )

        return super().validate(args)

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
