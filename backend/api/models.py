from django.db import models
from django.utils import timezone

# Create your models here.

# Pet Owner
class Owner(models.Model):
    """
    Model representing a owner.
    """
    name = models.CharField(max_length=100, help_text="Name")
    passport = models.CharField(max_length=13, null=True, help_text='Passport')
	
    def __str__(self):
        """
        String for representing the Model object
        """
        return self.name

# Favorite foods
class Food(models.Model):
    """
    Model representing a food.
    """
    name = models.CharField(max_length=150, help_text="Name")
    
    def __str__(self):
        """
        String for representing the Model object
        """
        return self.name

# Pet
class Pet(models.Model):
    """
    Model representing a pet.
    """
    date_in = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100, help_text="Name")
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)
    food = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
	
    TYPE = (
        ('op01', 'Gato'),
        ('op02', 'Perro'),
        ('op03', 'Loro'),
        ('op04', 'Que se yo'),
    )
	
    type = models.CharField(max_length=4, choices=TYPE, blank=False, default='0p01', help_text='Pet Type')
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name