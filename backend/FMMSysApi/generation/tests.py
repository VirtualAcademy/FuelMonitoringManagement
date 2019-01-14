from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import PowerPlant

# Create your tests here.


class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.plant_name = "SLL"
        self.location = "Songloulou"
        self.production_capacity = 250
        self.power_category = 1
        self.placement_priority = 1
        self.grouping = "Thermal"
        self.powerplant = PowerPlant(
            plant_name=self.plant_name,
            location=self.location,
            production_capacity=self.production_capacity,
            power_category=self.power_category,
            grouping=self.grouping,
            placement_priority=self.placement_priority,
            )

    def test_model_can_create_a_PowerPlant(self):
        """Test the PowerPlant model can create a Power Plant entry."""
        old_count = PowerPlant.objects.count()
        self.powerplant.save()
        new_count = PowerPlant.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        self.plant_name = "LPP"
        self.location = "Limbe"
        self.production_capacity = 200
        self.power_category = 1
        self.placement_priority = 2
        self.grouping = "Thermal"
        self.powerplant_data = dict(
            plant_name=self.plant_name,
            location=self.location,
            production_capacity=self.production_capacity,
            power_category=self.power_category,
            grouping=self.grouping,
            placement_priority=self.placement_priority,
            )

        self.power_plant = PowerPlant.objects.get()

    def test_api_can_create_a_power_plant(self):
        """Test the api has power plant creation capability."""
        self.response = self.client.post(
            reverse('power_plant'),
            self.powerplant_data,
            format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_power_plant(self):
        """Test the api can get a given power plant."""
        self.response = self.client.get(reverse('power_plant_details', kwargs={'pk': self.power_plant.id}), format="json")
        self.assertEqual(self.response.status_code,  status.HTTP_200_OK)
        self.assertContains(self.response, self.power_plant)

    def test_api_can_update_a_power_plant(self):
        """Test the api can update  a given power plant."""
        change_plant_name = {'plant_name': 'Limbe Power Plant'}
        self.response = self.client.put(reverse('power_plant_details', kwargs={'pk': self.power_plant.id}),
                                        change_plant_name, format="json")
        self.assertEqual(self.response.status_code,  status.HTTP_200_OK)

    def test_api_can_delete_a_power_plant(self):
        """Test the api can delete a given power plant."""
        self.response = self.client.delete(reverse('power_plant_details', kwargs={'pk': self.power_plant.id}), format="json", follow=True)
        self.assertEqual(self.response.status_code,  status.HTTP_204_NO_CONTENT)