from django.urls import path

from traductor.views import *

urlpatterns = [
    path('', TraductorView.as_view(), name='traductor')
]
