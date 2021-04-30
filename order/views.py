from django.shortcuts import render
from .models import Order

from .serializers import OrderSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class OrderListCreateView(APIView):
    def get(self, request, *args, **kwargs): #list all existing orders GET
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs): #create a new order POST
        serializer = OrderSerializer(data=request.POST)
        if serializer.is_valid():
            order_object = serializer.save()
            json_serializer = OrderSerializer(instance=order_object)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class OrderView(APIView):
    def get(self, request, *args, **kwargs): #list an individual order GET
        try:
            order = Order.objects.get(pk=kwargs.get('pk'))
        except Order.DoesNotExist as e:
            return Response(data={"message": f'Order was not found {e}'}, status=404)
        serializer = OrderSerializer(instance=order)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs): #update an individual order

        order = order = Order.objects.get(pk=kwargs.get('pk'))
        order_serialized = OrderSerializer(order, data=request.data)

        if order_serialized.is_valid():
            order_serialized.save()
            return Response(order_serialized.data, status=200)
        return Response(data=serializer.errors)


    def delete(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs.get('pk'))
        order.status = 2
        order.save()
        return Response(data={'message': 'Order was cancelled'})
        