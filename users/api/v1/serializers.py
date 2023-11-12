from rest_framework import serializers
from users.models import SignupUser
from allauth.utils import generate_unique_username
from rest_framework.validators import UniqueValidator



class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(SignupUser.objects.all(), message='This email already exists')])
    class Meta:
        model = SignupUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'school_email', 'school', 'grade', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            'username': {'required': False, 'read_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('password did not match')
        return data

    def create(self, validated_data):
        user = SignupUser(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            school_email=validated_data.get('school_email'),
            school=validated_data.get('school'),
            grade=validated_data.get('grade'),
            password=validated_data.get('password'),
            confirm_password=validated_data.get('confirm_password'),
            username=generate_unique_username([validated_data.get('first_name'),
                                               validated_data.get('last_name'),
                                               'user'
                                               ])


        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user



# Login user

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignupUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'school_email', 'school', 'grade','password', 'image']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only':True, 'required':False}
        }



# update or change password

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError('Password Did not Match')
        return data



class UserProfileImageChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignupUser
        fields = ['image']




class UserProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignupUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'school_email', 'school', 'grade','image']






