from django.db import models
from type.models import Type
from attack.models import Attack

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    health = models.IntegerField()
    poke_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    attacks = models.ManyToManyField(Attack)
