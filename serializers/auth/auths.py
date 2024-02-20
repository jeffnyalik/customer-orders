from rest_framework import serializers
from authentication.models import CustomUser
from django.contrib.auth import authenticate

class  UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user
    

# class UserLoginSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(max_length=200, min_length=3)
#     password = serializers.CharField(max_length=68, min_length=6, write_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password',)

#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         password = attrs.get('password', '')

#         user = authenticate(email=email, password=password)
#         if user is not None:
#             attrs['user'] = user
#             return attrs
        
#         else:
#             raise serializers.ValidationError("Invalid credentials")
    