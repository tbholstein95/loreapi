from rest_framework import serializers
from lore.models import Lore
from django.contrib.auth.models import User


class LoreSerializer(serializers.HyperlinkedModelSerializer):
	# Defines fields that are getting serializes/deserialized
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Lore
		fields = ['url', 'id', 'title', 'firstname', 'adventurerType', 'owner']

	# Define how complete instances are created or modified when using serializer.save
	def create(self, validated_data):
		"""
		Create and return a new 'Snippet' instance, given the validated data
		"""
		# TODO Objects highlighted yellow in Pycharm 2020.2 on 9/24/2020
		return Lore.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing Lore model instance, given the validated data
		"""
		instance.title = validated_data.get('title', instance.title)
		instance.firstname = validated_data.get('code', instance.firstname)
		instance.save()
		return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
	lore = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'lore']