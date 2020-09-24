from rest_framework import generics
from rest_framework import mixins

from lore.models import Lore
from lore.serializers import LoreSerializer


# Create your views here.
class LoreList(generics.ListCreateAPIView):
	queryset = Lore.objects.all()
	serializer_class = LoreSerializer


class CharacterEntryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Lore.objects.all()
	serializer_class = LoreSerializer
