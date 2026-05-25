from django.urls import path
from .views import emission_list, esg_score

urlpatterns = [
    path('', emission_list),
    path('score/', esg_score),
]