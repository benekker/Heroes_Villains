from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer
from rest_framework import status
from constants import GET, POST, PUT, DELETE
from django.shortcuts import get_object_or_404
from dictionary import heroes_dict, villains_dict

@api_view([GET, POST])
def supers_list(request):
    if request.method == GET:
        heroes = Super.objects.filter(super_type_id = 1)
        villains = Super.objects.filter(super_type_id = 2)
        supers_param = request.query_params.get('type')
        if supers_param:
            if supers_param == 'hero':
                serializer = SuperSerializer(heroes, many=True)
                return Response(serializer.data) 
            elif supers_param == 'villain':
                serializer = SuperSerializer(villains, many=True)
                return Response(serializer.data)
            else:
                output = 'No valid Super Type'
                return Response(output, status=status.HTTP_204_NO_CONTENT)
        else:
            heroes = heroes_dict(heroes)
            villains = villains_dict(villains)
            custom_dict_response = {'Heroes': heroes, 'Villains': villains}
            return Response(custom_dict_response)
    elif request.method == POST:
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view([GET, PUT, DELETE])
def get_super_by_id(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == GET:
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == PUT:
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == DELETE:
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

