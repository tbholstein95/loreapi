from rest_framework import generics, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from lore.serializers import UserSerializer
from lore.models import Lore
from lore.serializers import LoreSerializer
from rest_framework import permissions
from lore.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

# Create your views here.
class CharacterViewSet(viewsets.ModelViewSet):
	"""
	provides list, create, retrieve, update, and destroy
	"""
	queryset = Lore.objects.all()
	serializer_class = LoreSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_create(self,serializer):
		serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	Automatic list and detail actions
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer

# class ProfileDetail(APIView):
# 	renderer_classes = [TemplateHTMLRenderer]
# 	template_name = 'front_end.html'
#
# @api_view(['GET'])
# def api_root(request, format=None):
# 	return Response({
# 		'users': reverse('UserList', request=request, format=format),
# 		'lore': reverse('LoreList', request=request, format=format)
# 	})