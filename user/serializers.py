from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField(required=False)
    photo = serializers.ImageField(required=False)
    date_of_birth = serializers.DateField(required=False)

    class Meta:
        model = User
        fields = ['password', 'email', 'date_of_birth', 'username', 'photo', 'phone']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            phone=validated_data.get('phone'),
            date_of_birth=validated_data.get('date_of_birth'),
            photo=validated_data.get('photo')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        user.create_code()
        return user


class UserConfirmationSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4, required=True)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=25, required=True)
    password = serializers.CharField(max_length=256, required=True)

    def validate(self, attrs):
        user = authenticate(username=attrs.get('username'), password=attrs.get('password'))
        if user and user.is_verified:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token)
            }
        else:
            raise serializers.ValidationError("Login yoki parol xato yoki foydalanuvchi tasdiqlanmagan.")
        # return super().validate(attrs)



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phone', 'first_name', 'last_name', 'date_of_birth', 'photo']
        read_only_fields = ['username', 'is_verified']


