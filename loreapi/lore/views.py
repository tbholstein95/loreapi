from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from lore.serializers import UserSerializer
from lore.models import Lore
from lore.serializers import LoreSerializer
from rest_framework import permissions
from lore.permissions import IsOwnerOrReadOnly


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
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('UserList', request=request, format=format),
		'lore': reverse('LoreList', request=request, format=format)
	})