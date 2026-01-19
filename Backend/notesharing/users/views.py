from rest_framework import permissions, status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer, Userserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import  FormParser

User=get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer
    permission_classes=[permissions.AllowAny]

class CurrentUserView(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self, request):
        serializer=Userserializer(request.user)
        return Response(serializer.data)

class UpdateUserView(APIView):
    parser_classes=[FormParser]
    permission_classes=[IsAuthenticated]

    def patch(self, request):
        user= request.user
        data=request.data

        serializer=Userserializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)