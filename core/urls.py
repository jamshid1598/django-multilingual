from django.urls import path
from .views import HomePage

app_name = 'core'

urlpatterns = [
    path('', HomePage, name='home'),
]