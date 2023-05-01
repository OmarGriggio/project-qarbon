from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets, permissions
from .models import Message
from .serializers import UserSerializer, GroupSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event, Place
from .serializers import EventSerializer, PlaceSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

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


@api_view(['GET'])
def welcome_page(request):
    welcome_text = ["Bienvenue dans cette API que votre application peut consommer","Pour avoir une vue d'ensemble, ajoutez 'api/' à l'url"]
    return Response(welcome_text)

@api_view(['GET'])
def api_overview(request):
    api_urls = [
    "API vue d'ensemble : /api/",
    "Liste d'événements : api/event-list/",
    "Liste de lieux : api/place-list/",
    "Créer un compte : api/create-account/",
    "Ajouter un nouvel Evenement : api/event-create/",
    "Ajouter un nouveau lieu : api/place-create/"
    ]
    return Response(api_urls)
    
@api_view(['GET'])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def event_list_by_place(request, pk):
    events = Event.objects.raw("SELECT * FROM `django_rest_api_manager_event` join django_rest_api_manager_place on django_rest_api_manager_event.place_id = django_rest_api_manager_place.name where django_rest_api_manager_place.name = '"+ pk +"'")
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def place_list_by_event(request, pk):
    places = Place.objects.raw("SELECT django_rest_api_manager_place.name, street, number, postal_code, locality FROM `django_rest_api_manager_event` join django_rest_api_manager_place on django_rest_api_manager_event.place_id = django_rest_api_manager_place.name where django_rest_api_manager_event.name = '"+ pk +"'")
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def place_list(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def place_find(request, pk):
    places = Place.objects.get(name=pk)
    serializer = PlaceSerializer(places, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def event_create(request):
    serializer = EventSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def place_create(request):
    serializer = PlaceSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

