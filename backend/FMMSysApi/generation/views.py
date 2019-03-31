from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import PowerPlantSerializer, AutonomyLeftSerializer, HourlyTPASerializer, GeneratorsSerializer, \
	DemandSerializer, HourlyPFSerializer
from .models import PowerPlant, AutonomyLeft, HourlyTotalPowerAvailable, Generators, Demand, HourlyProductionForecast

listcreate = lambda s:"""
    This class creates a New %s or List all existing ones.
    get:
    Return a list of all the existing %s in the database.
    post:
    Create a new %s instance in the database.
    """ %(s for i in range(3))


class PowerPlantViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests.
    get:
    Return the details of  one Power Plant in the database.
    patch:
    Updates partially a given Power Plant instance in the database.
    put:
    Update a given Power Plant details
    delete:
    Removes or deletes a give Power Plant item from the database.
    """
    name = 'Modify Power Plan Details'

    queryset = PowerPlant.objects.all()
    serializer_class = PowerPlantSerializer


class AutonomyLeftViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests.
    get:
    Return the details of  one Autonomy Left in the database.
    patch:
    Updates partially a given Autonomy Left instance in the database.
    put:
    Update a given Autonomy Left details
    delete:
    Removes or deletes a give Autonomy Left item from the database."""
    name = 'Modify Autonomy Left Details'

    queryset = AutonomyLeft.objects.all()
    serializer_class = AutonomyLeftSerializer


class HourlyTPAViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Power Available Hourly Total Details'

    queryset = HourlyTotalPowerAvailable.objects.all()
    serializer_class = HourlyTPASerializer


class GeneratorsViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Generators Details'

    queryset = Generators.objects.all()
    serializer_class = GeneratorsSerializer


class DemandViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""
    name = 'Modify Demand Details'

    queryset = Demand.objects.all()
    serializer_class = DemandSerializer


class HourlyPFViewSet(viewsets.ModelViewSet):
    """This class handles the http GET, PUT and DELETE requests."""

    name = 'Modify Hourly Production Forecast Details'

    queryset = HourlyProductionForecast.objects.all()
    serializer_class = HourlyPFSerializer