from django.urls import path

from . import views

urlpatterns = [
    # ex: tenders
    path('', views.index, name='index'),
    # ex: tenders/id
    path('<int:tender_id>/', views.detail, name='detail'),
    # ex: tenders/newForOrganisation/organisation_id
    path('newForOrganisation/<int:organisation_id>/', views.newTender, name='new')
]