from rest_framework.serializers import ModelSerializer

from shop.models import Order


class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
