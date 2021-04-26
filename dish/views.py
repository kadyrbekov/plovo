from rest_framework.views import APIView

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Dish
from .serializers import DishListSerializer

from .models import Dish
from .serializers import DishListSerializer


class DishListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        dishes = Dish.objects.order_by('name')         
        dishes_serialized = DishListSerializer(dishes, many=True)        
        return Response(data=dishes_serialized.data)


class DishCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = DishCreateSerializer(data=data)
        if serializer.is_valid():
            dish_object = serializer.save()
            return Response(data={'message': 'The dish has been added'})
        return Response(data={'error': serializers.error})

    

class DishUpdateAPIView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        dish = Dish.objects.get(pk=pk)
        
        data = request.POST
        serializer = DishUpdateSerializer(data=data)
        
        if serializer.is_valid():
            dish.name = serializer.validated_data.get('name')
            dish.price = serializer.validated_data.get('price')
            dish.save()

            serialized_object = DishSerializer(data)
            data = serialized_object.data
            return Response(data=data)

        return Response(data=serializer.errors)