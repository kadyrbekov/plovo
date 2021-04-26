from rest_framework import serializers

from .models import Dish

class DishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'price', 'name')
    
class DishCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('price', 'name')
        
class DishUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('price', 'name')


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'price', 'name')