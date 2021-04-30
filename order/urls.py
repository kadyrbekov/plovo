from django.urls import path
from .views import OrderListCreateView, OrderView


urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'), # of /order/ + GET = list of orders, else if + POST = create new order
    path('<int:pk>/', OrderView.as_view(), name='order'), 
    path('<int:pk>/update/', OrderView.as_view(), name='update-order'),
    path('<int:pk>/delete/', OrderView.as_view(), name='delete-order'),

]