from django.urls import path
from lore import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
	path('', views.api_root),
	path('lore/',
	     views.LoreList.as_view(),
	     name='LoreList'),
	path('lore/<int:pk>/', views.CharacterEntryDetail.as_view(), name='lore-detail'),
	path('users/',
	     views.UserList.as_view(),
	     name='UserList'),
	path('users/<int:pk>/',
	     views.UserDetail.as_view(),
	     name='UserDetail')
])


