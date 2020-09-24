from django.db import models

# Create your models here.


class Lore(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	firstname = models.TextField()
	owner = models.ForeignKey('auth.User', related_name='lore', on_delete=models.CASCADE)
	highlighted = models.TextField()

	# Orders models by when they were created
	class Meta:
		ordering = ['created']
