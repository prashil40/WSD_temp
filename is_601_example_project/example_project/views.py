from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import BakedGood, BakedGoodForm, Ingredients
from django.urls import reverse
from rest_framework import viewsets
from rest_framework import permissions
from . import serializers

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")

def customPage(request):
    context = {
        'title': 'My Game Library',
        'data': [
            {
                'name': 'Ghost of Tsushima',
                'rating': 'NA',
            },
            {
                'name': 'Spiderman 2',
                'rating': '5/5',
            },
            {
                'name': 'Last of Us',
                'rating': '4.5/5',
            },
            {
                'name': 'Horizon Zero Dawn',
                'rating': '4.5/5',
            }
        ]
    }
    return render(request, 'index.html', context)

def bakeryPage(request):
    baked_goods = BakedGood.objects.all()
    context = {
        'title': 'Bakery',
        'data': baked_goods
    }
    return render(request, 'example_app/', context)


def bake(request):
    if request.method == 'POST':
        form = BakedGoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = BakedGoodForm()
    return render(request, 'bake.html', {'form': form})

def display_image(request):
    return render(request, 'display_image.html')

def ajax(request):
    return render(request, 'example_app/ajax.html')

def ajax_demo(request):
    data = {
        "this": 1,
        "is": 2,
        "JSON": 3,
    }

    return JsonResponse(data)

def my_ajax_view(request):
    data = []
    baked_goods = BakedGood.objects.all()
    for bg in baked_goods:
        data.append(bg._to_json())
    return JsonResponse({"bakedGood":data})


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]


class BakedGoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BakedGood.objects.all()
    serializer_class = BakedGoodSerializer
    permission_classes = [permissions.IsAuthenticated]