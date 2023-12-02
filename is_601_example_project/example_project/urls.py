from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('/myGameLibrary', views.customPage, name='page'),
#     path('/bake',views.bake, name='bake'),
#     path('/display_image', views.display_image, name='image'),
#     path('/ajax', views.ajax, name="ajax"),
#     path('/ajax_demo', views.ajax_demo, name="ajax_demo"),
#     path('/my_ajax_view', views.my_ajax_view, name="my_ajax_view"),
# ]


router = routers.DefaultRouter()
router.register(r'ingredients', views.IngredientViewSet)
router.register(r'bakedGood', views.BakedGoodViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]