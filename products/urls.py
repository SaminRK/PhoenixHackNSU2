from django.urls import path

from . import views

urlpatterns = [
    # ex: products
    path('', views.index, name='index'),
    # ex: products/id
    path('<int:product_id>/', views.detail, name='detail'),
    # ex: products/product_id/orderForOrganisation/org_id
    path('<int:product_id>/addOrderForOrganisation/<int:organisation_id>/', views.order, name='order')
]