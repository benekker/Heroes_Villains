from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer
from rest_framework import status
from constants import GET, POST, PUT, DELETE


@api_view([GET, POST])
def supers_list(request):

    if request.method == GET:
        supers = Super.objects.filter()


