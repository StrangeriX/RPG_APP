from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Attribute(models.Model):
    strenght = models.IntegerField(default=5)
    dextirity = models.IntegerField(default=5)
    inteligance = models.IntegerField(default=5)

class Skill(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    requirements = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Character(models.Model):
    CHOICES = (
        ('Human', "Human"),
        ('Elf', 'Elf'),
        ('Dwarf', 'Dwarf')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True, blank=False)
    race = models.CharField(max_length=150, blank=False, choices=CHOICES)
    level = models.IntegerField(default=1)
    attribute_points = models.IntegerField(default=10)
    skill_points = models.IntegerField(default=1)
    attributes = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, blank=True)
    experience = models.IntegerField(default=0)
    vitality = models.IntegerField(default=100)

    def __str__(self) -> str:
        return f'{self.name}, {self.race}'
