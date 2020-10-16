from django.db import models


# Create your models here.


class Lore(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	firstname = models.TextField()
	adventurerType = models.TextField()
	owner = models.ForeignKey('auth.User', related_name='lore', on_delete=models.CASCADE)

	# Orders models by when they were created
	class Meta:
		ordering = ['created']
