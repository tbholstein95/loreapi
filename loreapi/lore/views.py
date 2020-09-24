from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from lore.models import Lore
from lore.serializers import LoreSerializer


# Create your views here.
@csrf_exempt
def lore_list(request):
	"""

	List all Lore character identities, or create a new character
	"""
	if request.method == 'GET':
		lore = Lore.objects.all()
		serializer = LoreSerializer(lore, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = LoreSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def character_entry_detail(request, pk):
	"""
	Retrieve, update, or delete a character entry
	"""
	try:
		# TODO Objects highlighted yellow in Pycharm 2020.2 on 9/24/2020
		lore = Lore.objects.get(pk=pk)
	except Lore.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = LoreSerializer(lore)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = LoreSerializer(lore, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		lore.delete()
		return HttpResponse(status=204)
