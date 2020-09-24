from django.urls import path
from lore import views

urlpatterns = {
	path('lore/', views.lore_list),
	path('lore/<int:pk>/', views.character_entry_detail),
}