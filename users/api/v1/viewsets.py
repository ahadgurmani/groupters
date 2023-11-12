from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from users.models import SignupUser
from .serializers import SignupSerializer, UserLoginSerializer, ChangePasswordSerializer, \
    UserProfileImageChangeSerializer, UserProfileEditSerializer
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from fcm_django.models import FCMDevice


class UserSignupViewset(viewsets.ModelViewSet):
    serializer_class = SignupSerializer
    queryset = SignupUser.objects.none()



# Login user     and  login device for notifiaction

class UserLoginViewset(viewsets.ModelViewSet):
    serializer_class = AuthTokenSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        registration_id = request.data.get('registration_id')
        device_type = request.data.get('type')
        already = FCMDevice.objects.filter(registration_id=registration_id, type=device_type).first()
        if already:
            already.user = user
            already.save()
        else:
            FCMDevice.objects.create(registration_id=registration_id, type=device_type, user=user)
        user_details = UserLoginSerializer(user, many=False, context={'request': request})
        token, create = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_details': user_details.data})






# For All Users List and Change Password

class AllUsersViewset(viewsets.ModelViewSet):
    serializer_class = UserLoginSerializer
    queryset = SignupUser.objects.all()


    @action(detail=False, methods=['POST'])
    def change_password(self, request):
        serialier = ChangePasswordSerializer(data=request.data)
        if serialier.is_valid():
            user = request.user
            if user.check_password(serialier.validated_data["old_password"]):
                user.set_password(serialier.validated_data["new_password"])
                user.save()
                return Response({'msg': 'password updated successfully'})
            else:
                return Response({'msg': 'old password is not correct'})
        return Response(serialier.errors)


# action api for changing profile picture
    @action(detail=True, methods=['POST'])
    def profile_img_change(self, request, pk=None):
        user_obj = SignupUser.objects.filter(id=pk).first()
        serializer = UserProfileImageChangeSerializer(user_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": 'profile picture updated successfully'})


# action api for user profile edit
    @action(detail=True, methods=['POST'])
    def profile_edit(self, request, pk=None):
        user_obj = SignupUser.objects.filter(id=pk).first()
        serializer = UserProfileEditSerializer(user_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': 'Changes Saved Successfully'})





















