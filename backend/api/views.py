from django.contrib.auth.models import User, Group
from django.views.decorators.cache import never_cache
from rest_framework import viewsets, permissions
from .models import Message
from .serializers import UserSerializer, GroupSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from .models import Event, Place
from .serializers import EventSerializer, PlaceSerializer
from .filters import EventFilter, PlaceFilter
from dotenv import load_dotenv
from pathlib import Path
import requests
import os

# Load the .env file
load_dotenv()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # SHOULD IMPLEMENT CUSTOM PERMISSIONS FOR OBJECT LEVEL SECURITY

class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows places to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filterset_class = PlaceFilter
    # SHOULD IMPLEMENT CUSTOM PERMISSIONS FOR OBJECT LEVEL SECURITY

    @action(detail=False, methods=['get'])
    def search(self, request):
        print(os.getcwd())
        query = request.GET.get('query')
        api_key = os.getenv('GOOGLE_PLACES_API_KEY')
        print(api_key)
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={api_key}"
        response = requests.get(url)
        return Response(response.json())


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter
    # SHOULD IMPLEMENT CUSTOM PERMISSIONS FOR OBJECT LEVEL SECURITY
    
    # Ajoute auto le user authentifié comme user de l'event
    def create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        "messages": "http://127.0.0.1:8000/api/messages/",
        "users": "http://127.0.0.1:8000/api/users/",
        "groups": "http://127.0.0.1:8000/api/groups/",
        "events": "http://127.0.0.1:8000/api/events/",
        "places": "http://127.0.0.1:8000/api/places/",
    }
    return Response(api_urls)