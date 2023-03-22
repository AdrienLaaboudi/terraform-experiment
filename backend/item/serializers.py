from rest_framework import serializers

from item.models import Item


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return 'CATEGORY'

    def validate_name(self, value):
        if 'car' in value.lower():
            raise serializers.ValidationError("We don't sell cars, carrots or something with car.")
        return value

    def validate_price(self, value):
        if self.instance:
            if value < self.instance.cost:
                raise serializers.ValidationError("We need profit!")
            return value
        if value < int(self.initial_data.get('cost')):
            raise serializers.ValidationError("We need profit!")
        return value

    # def validate(self, data):
    #     raise serializers.ValidationError("Example")

    class Meta:
        model = Item
        # fields = '__all__'
        fields = ['id', 'name', 'price', 'cost', 'category']
        # write_only_fields = ['cost']
        # exclude = ['cost']
        extra_kwargs = {
            'cost': {'write_only': True},
        }


class ItemStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
