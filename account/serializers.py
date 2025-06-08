from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirmation = serializers.CharField(
        write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birth_date', 'email',
                  'organization', 'username', 'password', 'password_confirmation',
                  'scientific_degree', 'another_information', 'image')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise ValidationError(
                {"password": "password va password confirmation ga bir hil parol kiritilmadi"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            birth_date=validated_data.get('birth_date'),
            organization=validated_data.get('organization', ''),
            scientific_degree=validated_data.get('scientific_degree', ''),
            another_information=validated_data.get('another_information', ''),
            image=validated_data.get('image')
        )
        return user


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSeralizer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8)


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError({"xato": "Oldingi parol noto'g'ri"})
        return value
    