from rest_framework import serializers
from authentication.models import *
from django.contrib.auth import authenticate,login,get_user_model
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

# User = get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Company
        fields = '__all__'


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = EmployeeProfile
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Customer
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Vendor
        fields = '__all__'





User = get_user_model()


                                                    ########## register an user
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    token     = serializers.SerializerMethodField(read_only = True)
    message   = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password',
                  'password2',
                  'token',
                  'message']

        extra_kwargs = {
            'password':{'write_only':True}
        }


    def get_message(self,obj):
        return 'successfully registered'

    def get_token(self,obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        print(token)
        return token




    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password'],
        password2 = self.validated_data['password2'],

        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        user.set_password(password)
        user.save()
        return user







class LoginSerializer(serializers.ModelSerializer):

    username    = serializers.CharField(max_length=120)
    password    = serializers.CharField(style={'input_type':'password'},write_only=True)
    token       = serializers.SerializerMethodField(read_only = True)
    message     = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'token',
                  'message']

        extra_kwargs = {
            'password':{'write_only':True}
        }

    def get_message(self,obj):
        return 'successfully logged in'

    def get_token(self,obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        print(token)
        return token
#
#
# class RegistrationSerializer(serializers.ModelSerializer):
#     """Serialize registration requests and create a new user."""
#
#     # first_name = serializers.CharField()
#     # last_name = serializers.CharField()
#     # role = serializers.ChoiceField(
#     #     choices=[('CA', 'client_admin'),('VI', 'viewer')]
#     # )
#
#     password = serializers.CharField(
#         max_length=128,
#         min_length=6,
#         write_only=True,
#         error_messages={
#             "min_length": "Password should be at least {min_length} characters"
#         }
#     )
#
#     confirmed_password = serializers.CharField(
#         max_length=128,
#         min_length=6,
#         write_only=True,
#         error_messages={
#             "min_length": "Password should be at least {min_length} characters"
#         }
#     )
#
#     class Meta:
#         model = User
#         fields = ["email","password", "confirmed_password"]
#
#     def validate(self,data):
#
#         confirmed_password = data.get("confirmed_password")
#         try:
#             validate_password(data["password"])
#         except ValidationError as identifier:
#             raise serializers.ValidationError({
#             "password": str(identifier).replace("["", ""]", "")
#         })
#
#         if not self.do_passwords_match(data["password"], confirmed_password):
#             raise serializers.ValidationError({
#                 "passwords": ("Passwords do not match")
#         })
#
#         return data
#
#
#     def create(self, validated_data):
#         """ create user """
#         del validated_data["confirmed_password"]
#         return User.objects.create_user(**validated_data)
#
#     def do_passwords_match(self, password1, password2):
#         """Check if passwords match."""
#         return password1 == password2
#
# class LoginSerializer(serializers.Serializer):
#
#     email=serializers.EmailField()
#     password=serializers.CharField(
#         max_length=128, min_length=6, write_only=True, )
#     token=serializers.CharField(read_only=True)
#
#     def validate(self, data):
#         email=data.get("email", None),
#         password=data.get("password", None)
#         user=authenticate(username=email[0], password=password)
#         if user is None:
#             raise serializers.ValidationError({
#                 "invalid": "invalid email and password combination"
#             })
#         if UserDevices.objects.filter(user_id=user.id).exists():
#             raise serializers.ValidationError({
#                 "user": "User session already active on another device"
#             })
#         auth_token = user.token
#         u_session = UserDevices(user_id=user.id, token=auth_token)
#         u_session.save()
#         # if not user.is_verified:
#         #     raise serializers.ValidationError({
#         #         "user": "Your email is not verified,please vist your mail box"
#         #     })
#
#         user={
#             "email": user,
#             "token": auth_token
#         }
#         return user
