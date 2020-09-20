from django.urls import path

from . import views

urlpatterns = [
    # ex: organisations
    path('', views.index, name='index'),
    # ex: organisations/id
    path('<int:organisation_id>/', views.detail, name='detail'),
]