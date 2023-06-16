from django.urls import path
from .views import index, sistema

app_name = 'core'

urlpatterns = [
    path('', index, name='core-index'),
    path('admin/', sistema, name='core-sistema'),
]