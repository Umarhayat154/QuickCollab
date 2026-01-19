from rest_framework import serializers
from .models import User

class Userserializer(serializers.ModelSerializer):
    role=serializers.CharField(read_only=True)
    class Meta :
        model = User
        fields =('id', 'name','email','role','created_at','updated_at')

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=('id', 'name','email', 'password','password2','role')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password: password do not match'})
        return attrs
    
    def create(self, validated_data):
        password=validated_data.pop('password')
        validated_data.pop('password2')
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
        