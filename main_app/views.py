from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ExtendedUserView(viewsets.ModelViewSet):
    serializer_class = ExtendedUserSerializer
    queryset = ExtendedUser.objects.all()

class DisplayTypeView(viewsets.ModelViewSet):
    serializer_class = DisplayTypeSerializer
    queryset = DisplayType.objects.all()

class TimelineView(viewsets.ModelViewSet):
    serializer_class = TimelineSerializer
    queryset = Timeline.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class EntryView(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()