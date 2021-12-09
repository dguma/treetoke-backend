from django.urls import path
from .views import StrainsList

urlpatterns = [
    path('', StrainsList.as_view())
]