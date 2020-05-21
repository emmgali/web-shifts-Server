from django.urls import path

from .views import concepts


urlpatterns = [
    path('', concepts.index, name='concepts_index'),
    path('concepts', concepts.index, name="concepts_index2")
]