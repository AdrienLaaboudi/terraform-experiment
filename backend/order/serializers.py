from django.contrib.auth import get_user_model
from rest_framework import serializers

from item.serializers import ItemSerializer
from order.models import Order

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class OrderSerializer(serializers.ModelSerializer):
    # items = ItemSerializer(many=True, read_only=True)
    # buyer = UserSerializer(read_only=True)
    # buyer = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'buyer': {'read_only': True},
        }
        # depth = 1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = ItemSerializer(instance.items, many=True).data
        representation['buyer'] = UserSerializer(instance.buyer).data
        return representation
