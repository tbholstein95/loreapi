from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User
from lore.serializers import UserSerializer
from lore.models import Lore
from lore.serializers import LoreSerializer
from rest_framework import permissions


# Create your views here.
class LoreList(generics.ListCreateAPIView):
	queryset = Lore.objects.all()
	serializer_class = LoreSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class CharacterEntryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Lore.objects.all()
	serializer_class = LoreSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer