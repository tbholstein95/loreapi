from rest_framework import serializers
from lore.models import Lore


class LoreSerializer(serializers.ModelSerializer):
	# Defines fields that are getting serializes/deserialized
	class Meta:
		model = Lore
		fields =['id', 'title', 'firstname']

	# Define how complete instances are created or modified when using serializer.save
	def create(self, validated_data):
		"""
		Create and return a new 'Snippet' instance, given the validated data
		"""
		return Lore.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing Lore model instance, given the validated data
		"""
		instance.title = validated_data.get('title', instance.title)
		instance.firstname = validated_data.get('code', instance.firstname)
		instance.save()
		return instance