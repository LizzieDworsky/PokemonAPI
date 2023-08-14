from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'health', 'poke_type', 'poke_type_id', 'attacks']
        depth = 1
    poke_type_id = serializers.IntegerField(write_only=True)
    # attacks_id = serializers.IntegerField(write_only=True)