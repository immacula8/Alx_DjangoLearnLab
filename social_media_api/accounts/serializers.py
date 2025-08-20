from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)  # return token after registration

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'token']

    def create(self, validated_data):
        # ✅ use get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # ✅ explicitly create a token
        token = Token.objects.create(user=user)
        # attach token to user instance for serializer output
        user.token = token.key
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            # ✅ explicitly create/get token here too
            token, created = Token.objects.get_or_create(user=user)
            return {
                "username": user.username,
                "email": user.email,
                "token": token.key
            }
        raise serializers.ValidationError("Invalid credentials")
