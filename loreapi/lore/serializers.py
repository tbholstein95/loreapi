from rest_framework import serializers
from lore.models import Lore
from django.contrib.auth.models import User


class LoreSerializer(serializers.HyperlinkedModelSerializer):
	# Defines fields that are getting serializes/deserialized
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Lore
		fields = ['url', 'id', 'firstname', 'adventurerType', 'owner']

	# Define how complete instances are created or modified when using serializer.save
	def create(self, validated_data):
		"""
		Creates new character
		"""
		# TODO Objects highlighted yellow in Pycharm 2020.2 on 9/24/2020
		return Lore.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing Lore model instance, given the validated data
		"""
		instance.firstname = validated_data.get('firstname', instance.firstname)
		instance.adventurerType = validated_data.get('adventurerType', instance.adventurerType)
		instance.save()
		return instance

	def validate_firstname(self, data):
		x = data.isalpha()
		print(data)
		print(x)
		if not x:
			raise serializers.ValidationError("Names may only contain letters.")
		return data

	def validate_adventurerType(self, data):
		x = data.isalpha()
		print(data)
		print(x)
		if not x:
			raise serializers.ValidationError("Names may only contain letters.")
		return data


class UserSerializer(serializers.HyperlinkedModelSerializer):
	lore = serializers.HyperlinkedRelatedField(many=True, view_name='lore-detail', read_only=True)

	class Meta:
		model = User
		fields = ['url', 'id', 'username', 'lore']