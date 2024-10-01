from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.db import transaction


class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "phone", "description", 'stripeCustomerId', 'stripeSubscriptionId',
                  'stripeSubscriptionStatus', 'stripePriceId',
                  "is_active", "email", "created_at", "updated_at"]


class UserUpdateStripeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['stripeCustomerId', 'stripeSubscriptionId',
                  'stripeSubscriptionStatus', 'stripePriceId']


class UserFlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", 'stripeCustomerId', 'stripeSubscriptionId',
                  'stripeSubscriptionStatus', 'stripePriceId']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ["id", "email", "phone", "description",
                  "is_active", "password", "name", "last_name",
                  "first_name", "created_at", "updated_at"]
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        with transaction.atomic():
            password = validated_data.pop("password")
            first_name = validated_data.get("first_name", "")
            last_name = validated_data.get("last_name", "")
            user = User.objects.create(**validated_data)
            user.set_password(password)

            if first_name and last_name:
                user.name = f"{first_name} {last_name}".strip()
            else:
                user.name = validated_data.get("name", "")

            user.save()
            return user


class UserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])

        instance.save()

        return instance


class UserCompleteReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "phone",
            "description",
            "is_active",
            "name",
            "last_name",
            "first_name",
            'stripeCustomerId',
            'stripeSubscriptionId',
            'stripeSubscriptionStatus',
            'stripePriceId',
            "created_at",
            "updated_at",
        ]


class WithUserRegisterSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        with transaction.atomic():
            user_data = validated_data.pop("user")
            user_data["is_active"] = True
            password = user_data.pop("password")

            user = UserRegisterSerializer.create(
                UserRegisterSerializer(), validated_data=user_data
            )
            user.set_password(password)
            user.save()
            validated_data["user"] = user

            return super().create(validated_data)


class ProfileTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data["user"] = UserCompleteReadOnlySerializer(self.user).data

        return data
