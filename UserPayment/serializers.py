from django.contrib.auth.models import User
from rest_framework import serializers

class BillingAddressSerializer(serializers.Serializer):
    email_address = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
