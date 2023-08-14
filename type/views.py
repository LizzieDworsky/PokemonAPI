from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Type
from .serializer import TypeSerializer

# Create your views here.
@api_view(['GET'])
def all_pokemon_types(request):
    type_list = Type.objects.all()
    serializer = TypeSerializer(type_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)