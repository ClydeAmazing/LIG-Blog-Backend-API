from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from api.serializers import RegistrationSerializer, LoginSerializer

from rest_framework.response import Response

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    serializer = LoginSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = User.objects.get(email=serializer.validated_data['email'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'token_type': "bearer"},
                    status=HTTP_200_OK)
    else:
        data['message'] = 'The given data was invalid.'
        data['errors'] = serializer.errors
        return Response(data=data, status=HTTP_422_UNPROCESSABLE_ENTITY)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    response_status = HTTP_200_OK

    if serializer.is_valid():
        serializer.save()
        account = User.objects.get(email=serializer.validated_data['email'])
        data['id'] = account.id
        data['name'] = serializer.validated_data['name']
        data['email'] = serializer.validated_data['email']
        
    else:
        data['message'] = "The given data was invalid."
        data['errors'] = serializer.errors
        response_status = HTTP_422_UNPROCESSABLE_ENTITY

    return Response(data, status=response_status)
