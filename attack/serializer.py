from rest_framework import serializers
from .models import Attack

class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = ['id', 'name', 'power']