from django.db import models

class Animal(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    rfid_tag = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Health(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    condition = models.CharField(max_length=100)
    treatment = models.TextField()
    veterinarian = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

class Breeding(models.Model):
    mother = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='mother_breedings')
    father = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='father_breedings')
    breeding_date = models.DateField()
    expected_date = models.DateField()
    success = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
