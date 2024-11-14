from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from user.serializers import UserRegistrationSerializer, UserConfirmationSerializer


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


class VerifyUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=UserConfirmationSerializer
    )
    def post(self, request):
        user = request.user
        serializer = UserConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data.get('code')
            print(user, code)
            return Response(
                data={
                    'success': True,
                    'access': user.token()['access'],
                    'refresh': user.token()['refresh_token']
                }
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

