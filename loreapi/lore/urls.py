from django.urls import path, include
from lore import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'lore', views.CharacterViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
	path('', include(router.urls))
]