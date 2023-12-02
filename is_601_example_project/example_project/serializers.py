from .models import BakedGood, Ingredients
from rest_framework import serializers


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredients
        fields = [
            'name',
            'desc',
        ]


class BakedGoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BakedGood
        fields = [
            'name',
            'desc',
            'good_type',
            'price',
            'recipe',
            'ingredients',
            'baked_on',
        ]
