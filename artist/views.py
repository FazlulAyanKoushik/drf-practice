"""
    Views for Artist
"""
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from artist.serializer import UserSerializer, ArtistSerializer
from django.contrib.auth import get_user_model

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

User = get_user_model()

"""Create Views Here"""
class ArtistRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(pk=response.data['id'])
        artist_data = {'user': user.id, 'age': request.data['age']}
        artist_serializer = ArtistSerializer(data=artist_data)
        if artist_serializer.is_valid():
            artist_serializer.save()
            return Response(artist_serializer.data, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)