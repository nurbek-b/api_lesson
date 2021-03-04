from django.urls import path
from .views import CompanyView, CompanyCreate, CompanyDetail


urlpatterns = [
    path('list/', CompanyView.as_view(), name='company_list'),
    path('create/', CompanyCreate.as_view(), name='company_create'),
    path('<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
]