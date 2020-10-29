from django.urls import path

from . import views

app_name = "product"

urlpatterns = [
    # ex: /product/
    path('', views.index, name='index'),
    
    # ex: /product/5/
    path('<int:device_id>/', views.detail, name='detail'),
    
    # ex: /product/5/results/
    path('<int:device_id>/results/', views.test_results, name='test_results'),
    
    # ex: /product/5/new/
    path('<int:device_id>/new/', views.new_entry, name='new_entry'),
]