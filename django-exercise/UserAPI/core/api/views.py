from rest_framework.views import APIView
from core.api.serializers import UserCreateSerializer, UserListSerializer
from core.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


class UserClassBaseView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # verilerin alınması
        # veriler serializer ile validate
        # user oluşturulacak.
        user_data = request.data
        serializer = UserCreateSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise serializers.ValidationError(serializer.errors)

    def put(self, request, pk, format=None):
        user_data = request.data
        user = User.objects.get(id=pk)
        serializer = UserCreateSerializer(data=user_data)
        if serializer.is_valid():
            serializer.update(user, serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise serializers.ValidationError(serializer.errors)

    def patch(self, request, pk, format=None):
        user_data = request.data,
        user = User.objects.get(id=pk)
        serializer = UserCreateSerializer(data=user_data)
        if serializer.is_valid():
            serializer.update(user, serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        raise serializers.ValidationError(serializer.errors)
    
    def delete(self, request, pk, format=None):
        try:
            user = User.objects.get(id = pk)
            user.delete()
        except:
            raise serializers.ValidationError("Kullanıcı bulunamadı.")
        return Response(status=status.HTTP_204_NO_CONTENT)