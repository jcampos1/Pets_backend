# Create your views here.

from api.models import Owner, Food, Pet
from rest_framework import viewsets
from api.serializers import OwnerSerializer, FoodSerializer, PetSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows owners to be viewed or edited.
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows foods to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class PetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pets to be viewed or edited.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer