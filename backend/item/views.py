from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from item.models import Item
from item.permissions import IsStaffOrReadOnly, IsSuperuserOrReadOnly
from item.serializers import ItemSerializer, ItemStaffSerializer


class ListCreateItemView(ListCreateAPIView):
    """
    post:
    this is the title

    # subtitle
    this *is* the **description**
    """
    queryset = Item.objects.all()
    # permission_classes = [AllowAny]
    permission_classes = [IsStaffOrReadOnly]

    # permission_classes = [IsAuthenticated, IsStaffOrReadOnly] # AND
    # permission_classes = [IsAuthenticated | IsStaffOrReadOnly] # OR
    # permission_classes = [~IsAuthenticated] # NOT

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return ItemStaffSerializer
        return ItemSerializer


class RetrieveUpdateDeleteItemView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'
    permission_classes = [IsSuperuserOrReadOnly]
