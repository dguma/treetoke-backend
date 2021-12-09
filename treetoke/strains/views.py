from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StrainsSerializer
from .models import Strains

# Create your views here.

def index(request):
    return render(request, 'treetoke/index.html')


class StrainsList(viewsets.ModelViewSet):
    queryset = Strains.objects.all()[0:100]
    serializer_class = StrainsSerializer