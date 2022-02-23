from rest_framework import serializers
from .models import *



class RegisterApiSerializer(serializers.ModelSerializer):

    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        user=User(
            email=self.validated_data['email'],
            # firstname=self.validated_data['username'],

        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password !=password2:
            raise serializers.ValidationError({'password':"passoword must match"})

        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=50)
    password=serializers.CharField(max_length=40)

class CompanySerializer(serializers.ModelSerializer):
   # project_link = TeamSerializer(many=True)

    class Meta:
          model         =           Company
          fields        =          '__all__'

class ContactpersonSerializer(serializers.ModelSerializer):
   # project_link = TeamSerializer(many=True)

    class Meta:
          model         =           ContactPerson
          fields        =          '__all__'

class PositionSerializer(serializers.ModelSerializer):
   # project_link = TeamSerializer(many=True)

    class Meta:
          model         =           Position
          fields        =          '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department 
        fields='__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Business 
        fields='__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer 
        fields=['first_name','last_name','email_id','contact','address_1','city','state','country','zip_code','customer_id']

class DashboardSerializer(serializers.ModelSerializer):
    pass
   