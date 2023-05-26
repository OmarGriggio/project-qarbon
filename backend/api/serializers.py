from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.db.models import Avg
from .models import Message, Place, Event, Profile, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'rated_by', 'rating']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     profile = ProfileSerializer()
#     average_rating = serializers.SerializerMethodField()

#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         Profile.objects.create(user=user)
#         return user

#     def get_average_rating(self, obj):
#         average = obj.ratings_received.aggregate(Avg('rating'))['rating__avg']
#         if average is None:
#             return 0
#         return round(average, 1)
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'groups', 'password', 'profile', 'average_rating']
    #     extra_kwargs = {'password': {'write_only': True}}
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user)
        return user

    def get_average_rating(self, obj):
        average = obj.ratings_received.aggregate(Avg('rating'))['rating__avg']
        if average is None:
            return 0
        return round(average, 1)

    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'password', 'profile', 'average_rating']
        extra_kwargs = {'password': {'write_only': True}}


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

class UserStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

# Serializers pour afficher les participants d'un événement
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    user = UserStringSerializer(read_only=True)
    participants = UserRegisterSerializer(many=True, read_only=True)
    place = PlaceSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ['id','name', 'description','price', 'date', 'image', 'place', 'user', 'participants', 'capacity']
        # On récupère l'utilisateur authentifié donc pas besoin de faire un POST avec la pk.
        # Utilisateur automatiquement associé avec le token JWT dans le requête
        read_only_fields = ('user',)