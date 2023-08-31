from django.shortcuts import render
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import RegisterSerializer, UsertableSerializer

from authentication.models import Usertable
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset= Usertable.objects.all()
    serializer_class = UsertableSerializer
    permission_classes=[IsAuthenticated]

class UserLogIn(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token[0].key,
            'email': user.pk
        })

class RegisterAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer