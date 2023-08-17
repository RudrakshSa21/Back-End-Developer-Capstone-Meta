from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Menu
from .models import Booking
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = ['id','title','price','inventory']
