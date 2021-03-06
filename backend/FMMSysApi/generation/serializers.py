
from rest_framework import serializers
from .models import PowerPlant, AutonomyLeft, HourlyTotalPowerAvailable, Generators, Demand, HourlyProductionForecast


class PowerPlantSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = PowerPlant
		fields = ('url','id', "plant_name", "location", 'production_capacity', 'power_category', 'placement_priority', 'grouping')


class AutonomyLeftSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = AutonomyLeft
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		depth = 1


class HourlyTPASerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = HourlyTotalPowerAvailable
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		depth = 1


class GeneratorsSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Generators
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		depth = 1


class DemandSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Demand
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')


class HourlyPFSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = HourlyProductionForecast
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		depth = 1