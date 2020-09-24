from django.urls import path
from lore import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
	path('lore/', views.lore_list.as_view()),
	path('lore/<int:pk>/', views.character_entry_detail.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
