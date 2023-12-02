from django.db import models
from django.forms import ModelForm

# Create your models here.

class Ingredients(models.Model):
    name=models.CharField(max_length=64)
    desc=models.CharField(max_length=256)

class BakedGood(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    good_type = models.CharField(
        max_length=2,
        choices=[
            ('BG',"Bagel"),
            ('BR',"Bread"),
            ('CO',"Cookie"),
            ('CA',"Cake"),
            ('PR',"Pretzel")
        ]
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recipe = models.TextField()
    ingredients = models.ManyToManyField(Ingredients)
    baked_on = models.DateTimeField()

    def _to_json(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "good_type": self.good_type,
            "price": self.price,
            "recipe": self.recipe,
            # "ingredients": self.ingredients,
        }


class BakedGoodForm(ModelForm):
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
