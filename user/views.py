from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from user.serializers import UserRegistrationSerializer


class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=UserRegistrationSerializer
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'User created successfully',
                'detail': {
                    'username': user.username,
                    'email': user.email,
                    'phone_number': user.phone,
                    'refresh_token': user.token()['refresh_token'],
                    'access_token': user.token()['access']
                }
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

