from django.contrib import admin

from .models import BakedGood, Ingredients

admin.site.register(BakedGood)
admin.site.register(Ingredients)