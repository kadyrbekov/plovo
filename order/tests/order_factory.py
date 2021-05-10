import factory 
from order.models import Order
from dish.tests import DishFactory

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    user = factory.Sequence(lambda n: f"User id: {n}")
    dish = factory.SubFactory(DishFactory)
    location = factory.Sequence(lambda n:)

    '''
    {
        "id": 3,
        "location": "Ahunbaeva Sovetskay",
        "phone": "0554393939",
        "status": 0,
        "user": null,
        "dish": 4
    },
    '''