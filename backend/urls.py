"""djangoHeroku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, UserViewSet, GroupViewSet, MessageViewSet, EventViewSet
from .api import views

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    # http://localhost:8000/
    path('', views.welcome_page, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    #path('api/', include(router.urls)),
    path('api/', views.api_overview, name="API"),

    path('api/explorer/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),

    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

    # http://localhost:8000/api/event-list/
    path('api/event-list/', views.event_list, name="Liste des évènements"),

    # http://localhost:8000/api/place-list/
    path('api/place-list/', views.place_list, name="Liste des lieux"),

    # http://localhost:8000/api/place-find/
    path('api/place-find/<str:pk>/', views.place_find, name="Détails d'un lieu"),

    # http://localhost:8000/api/place-find/
    path('api/event-find/<str:pk>/', views.event_find, name="Détails d'un event"),

    # http://localhost:8000/api/event-create/
    path('api/event-create/', views.event_create, name="Ajout d'un évènement"),

    # http://localhost:8000/api/place-create/
    path('api/place-create/', views.place_create, name="Ajout d'un lieu"),

    # http://localhost:8000/api/events-find-by-place/
    path('api/events-find-by-place/<str:pk>/', views.event_list_by_place, name="Liste des evenements d'après un lieu"),

    # http://localhost:8000/api/places-find-by-event/
    path('api/places-find-by-event/<str:pk>/', views.place_list_by_event, name="Liste des endroits ou ont (eu) lieu un événement"),


    # 
    path('events/', EventViewSet.as_view({'get': 'list'}), name='events'),
]
