from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated

from account.models import User
from config import settings
from .serializers import RegisterSerializer, PasswordResetSerializer, PasswordResetConfirmSeralizer, PasswordChangeSerializer, ProfileViewSerializer, UserUpdateProfileSerializer


class RegisterView(APIView):

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Muvaffaqiyatli ro'yxatdan o'tdingiz"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):

    @swagger_auto_schema(request_body=PasswordResetSerializer)
    def post(self, request):
        serailizer = PasswordResetSerializer(data=request.data)
        if serailizer.is_valid():
            email = serailizer.validated_data['email']

            try:
                user = User.objects.get(email=email)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)

                parol_reset = f"http://127.0.0.1:8000/api/account/reset-password-confirm/?uid={uid}&token={token}"

                send_mail(
                    'Parolni tiklash',
                    f"Parolni yangilash uchun manashu linkni bosing:\n{parol_reset}",
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                return Response({"message": "emailga parolni tiklash uchun link yuborildi"}, status=200)

            except User.DoesNotExist:
                return Response(serailizer.errors, status=404)

        return Response(serailizer.errors, status=400)


class PasswordResetConfirmView(APIView):

    @swagger_auto_schema(request_body=PasswordResetConfirmSeralizer)
    def post(self, request):
        serializer = PasswordResetConfirmSeralizer(data=request.data)
        if serializer.is_valid():
            uid = serializer.validated_data['uid']
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']

            try:
                uid = force_str(urlsafe_base64_decode(uid))
                user = User.objects.get(pk=uid)

                if default_token_generator.check_token(user, token):
                    user.set_password(new_password)
                    user.save()
                    return Response({"message": "Parol yangilandi"}, status=200)
                else:
                    return Response({"error": "Token xato yoki eskirgan"}, status=400)

            except (User.DoesNotExist, ValueError):
                return Response({"error": "Foydalanuvchi topilmadi"}, status=404)

        return Response(serializer.errors, status=400)


class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=PasswordChangeSerializer)
    def post(self, request):
        serializer = PasswordChangeSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': "Parol muvoffaqiyatli o'rgartirildi"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = ProfileViewSerializer(user)
        return Response(serializer.data)


class UserUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=UserUpdateProfileSerializer)
    def put(self, request):
        user = request.user
        serializer = UserUpdateProfileSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
