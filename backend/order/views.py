from django.db import transaction
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from item.models import Item
from order.models import Order, OrderedItems
from order.permissions import IsBuyer
from order.serializers import OrderSerializer


class ListCreateOrderView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        # Create the order object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save(buyer=request.user)

        # Extract items and quantities from the request data
        items_data = request.data['items']
        # Create the ordered items and relate them to the order
        for item_data in items_data:
            item = get_object_or_404(Item, id=item_data['id'])
            ordered_item = OrderedItems.objects.create(order=order, item=item, quantity=item_data['quantity'])
            ordered_item

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDeleteOrderView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    permission_classes = [IsBuyer]
