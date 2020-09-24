from lore.models import Lore
from lore.serializers import LoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class lore_list(APIView):
	"""

	List all Lore character identities, or create a new character
	"""
	def get(self, request, format=None):
		lore = Lore.objects.all()
		serializer = LoreSerializer(lore, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = LoreSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class character_entry_detail(APIView):
	"""
	Retrieve, update, or delete a character entry
	"""
	def get_object(self, pk):
		try:
			# TODO Objects highlighted yellow in Pycharm 2020.2 on 9/24/2020
			return Lore.objects.get(pk=pk)
		except Lore.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		lore = self.get_object(pk)
		serializer = LoreSerializer(lore)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		lore = self.get_object(pk)
		serializer = LoreSerializer(lore, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		lore = self.get_object(pk)
		lore.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
