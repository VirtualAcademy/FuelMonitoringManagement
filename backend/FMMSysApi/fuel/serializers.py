
from rest_framework import serializers
from .models import Consumption, DailyProductionOnFuel, DeliveryOrder, Fuel, Inventory, SpecificConsumption, StockVariation, StorageUnit, Supplier, Supply, SupplyScheduleTransaction


class ConsumptionSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Consumption
		fields = '__all__'
		# depth = 1


class DailyProductionOnFuelSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = DailyProductionOnFuel
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		# depth = 1


class DeliveryOrderSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = DeliveryOrder
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		# depth = 1


class FuelSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Fuel
		fields = '__all__'


class InventorySerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Inventory
		fields = '__all__'
		read_only_fields = ('id','date_created', 'date_modified')
		# depth = 1


class SpecificConsumptionSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = SpecificConsumption
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		# depth = 1


class StockVariationSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = StockVariation
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		# depth = 1


class SupplyScheduleTransactionSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = SupplyScheduleTransaction
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		# depth = 1


class SupplySerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Supply
		fields = '__all__'
		read_only_fields = ('date_created', 'date_modified')
		# depth = 1


class StorageUnitSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = StorageUnit
		fields = '__all__'
		# depth = 1


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
	"""Serializer to map the Model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the model fields."""
		model = Supplier
		fields = '__all__'