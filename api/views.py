from django.shortcuts import render
from rest_framework import viewsets
from api.models import company
from api.serializers import companyserial
# Create your views here.
class apiview(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companyserial