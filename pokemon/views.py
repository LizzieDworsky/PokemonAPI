from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pokemon
from .serializer import PokemonSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def all_pokemon(request):                                                   #passing in the request
    if request.method == "GET":                                             #checking the request type
        pokemon_list = Pokemon.objects.all()                                #querying the database for all objects in the Pokemon table
        if request.query_params.get('type') == 'water':
            pokemon_list = pokemon_list.filter(poke_type__name="Water")
        elif request.query_params.get('type') == 'fire':
            pokemon_list = pokemon_list.filter(poke_type__name="Fire")
        elif request.query_params.get('type') == 'grass':
            pokemon_list = pokemon_list.filter(poke_type__name="Grass")
        serializer = PokemonSerializer(pokemon_list, many=True)             #serializing the data (to json) using two params Pokemons is the array of data retrieved on previous line, many=True is telling it to anticipate multiple objects
        return Response(serializer.data, status=status.HTTP_200_OK)         #responding to the request with the serialized data and the hard coded 200 status
    elif request.method == "POST":                                          #checking the request type
        serializer = PokemonSerializer(data=request.data)                   #converting the json data passed in through the POST method to python object data
        serializer.is_valid(raise_exception=True)                           #checking if the data is valid before the next step
        serializer.save()                                                   #once the object data has been verified, saving it to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)    #responding to the request with new data added and the hard coded 201 status


# @api_view(['GET'])
# def dictionary_params_get_all(request):
        # Querying once to get all records
        queryset = Super.objects.all()
        # Filtering the queryset (cached queryset - doesnt require another SQL execution)
        heroes = queryset.filter(super_type__type='Hero')
        villains = queryset.filter(super_type__type='Villain')
        heroes_serialized = SuperSerializer(heroes, many=True)
        villains_serialized = SuperSerializer(villains, many=True)
        if request.query_params.get('type') == 'hero':
            # Returns an array of objects (where type == hero)
            custom_response = heroes_serialized.data
        elif request.query_params.get('type') == 'villain':
            # Returns an array of objects (where type == villain)
            custom_response = villains_serialized.data
        else:
            # If neither if/elif triggered, respond with a custom formmated response (list of heroes in heroes key/ list of villains in villains key)
            custom_response = {
                'heroes': heroes_serialized.data,
                'villains': villains_serialized.data
            }
        return Response(custom_response)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def pokemon_by_id(request, pk):                                             #passing in the request and primary key(pk from the url)
    single_pokemon = get_object_or_404(Pokemon, pk=pk)                      #querying the database for one object using the pk(primary key)

    if request.method == "GET":                                             #checking the request type
        serializer = PokemonSerializer(single_pokemon)                      #serializing the Pokemon data from the database
        return Response(serializer.data, status=status.HTTP_200_OK)         #responding to the request with the serialized data of that single object and the hard coded status of 200
    elif request.method == "PUT":                                           #checking request type
        serializer = PokemonSerializer(single_pokemon, data=request.data)   #converting the json data passed in to a python object
        serializer.is_valid(raise_exception=True)                           #validating the data
        serializer.save()                                                   #saving the data after validation
        return Response(serializer.data, status=status.HTTP_200_OK)         #responding to the request with the serialized data and hard coded 200 status 
    elif request.method == "PATCH":                                           #checking request type
        serializer = PokemonSerializer(single_pokemon, data=request.data, partial=True)   #converting the json data passed in to a python object
        serializer.is_valid(raise_exception=True)                           #validating the data
        serializer.save()                                                   #saving the data after validation
        return Response(serializer.data, status=status.HTTP_200_OK)         #responding to the request with the serialized data and hard coded 200 status 
    elif request.method == "DELETE":                                        #checking request type
        single_pokemon.delete()                                             #removing the data permanently from the database
        return Response(status=status.HTTP_204_NO_CONTENT)                  #responding to the request with status 204, used as a confirmation the content has been removed from the database
