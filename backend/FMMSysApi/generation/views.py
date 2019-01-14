from django.shortcuts import render
from rest_framework import generics
from .serializers import PowerPlantSerializer, AutonomyLeftSerializer, HourlyTPASerializer, GeneratorsSerializer, \
	DemandSerializer, HourlyPFSerializer
from .models import PowerPlant, AutonomyLeft, HourlyTotalPowerAvailable, Generators, Demand, HourlyProductionForecast


class CreatePowerPlantView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api.
            get:
                Return a list of all the existing Power Plant.
            post:
                Create a new Power Plant instance.
    """
    name = 'Power Plants'
    queryset = PowerPlant.objects.all()
    serializer_class = PowerPlantSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Power plant."""
        serializer.save()


class PowerPlantDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Power Plan Details'

    queryset = PowerPlant.objects.all()
    serializer_class = PowerPlantSerializer


class CreateAutonomyLeftView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api.
            get:
                Return a list of all the existing Autonomy Left.
            post:
                Create a new Autonomy Left instance."""

    name = 'Create Autonomy Left'
    queryset = AutonomyLeft.objects.all()
    serializer_class = AutonomyLeftSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Power plant."""
        serializer.save()


class AutonomyLeftDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Autonomy Left Details'

    queryset = AutonomyLeft.objects.all()
    serializer_class = AutonomyLeftSerializer


class CreateHourlyTPAView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api.
            get:
                Return a list of all the existing Power Available Hourly Total.
            post:
                Create a new Power Available Hourly Total instance."""

    name = 'Create Power Available Hourly Total'
    queryset = HourlyTotalPowerAvailable.objects.all()
    serializer_class = HourlyTPASerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Power plant."""
        serializer.save()


class HourlyTPADetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Power Available Hourly Total Details'

    queryset = HourlyTotalPowerAvailable.objects.all()
    serializer_class = HourlyTPASerializer


class CreateGeneratorsView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api.
            get:
                Return a list of all the existing Generators.
            post:
                Create a new Generator instance."""
    name = 'Create Generators'
    queryset = Generators.objects.all()
    serializer_class = GeneratorsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Power plant."""
        serializer.save()


class GeneratorsDetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Generators Details'

    queryset = Generators.objects.all()
    serializer_class = GeneratorsSerializer


class CreateDemandView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api.
            get:
                Return a list of all the existing Demand.
            post:
                Create a new Demand instance."""
    name = 'Create Demand'
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Power plant."""
        serializer.save()


class DemandDetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Demand Details'

    queryset = Demand.objects.all()
    serializer_class = DemandSerializer


class CreateHourlyPFView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api.
            get:
                Return a list of all the existing Hourly Production Forecast.
            post:
                Create a new Hourly Production Forecast instance."""
    name = 'Create Hourly Production Forecast'
    queryset = HourlyProductionForecast.objects.all()
    serializer_class = HourlyPFSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Power plant."""
        serializer.save()

class HourlyPFDetailstView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    name = 'Modify Hourly Production Forecast Details'

    queryset = HourlyProductionForecast.objects.all()
    serializer_class = HourlyPFSerializer