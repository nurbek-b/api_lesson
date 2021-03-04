from django.urls import path
from .views import (CompanyView, CompanyCreate, CompanyDetail,
                    AdView, AdCreate, AdDetail)


urlpatterns = [
    # Company end points
    path('company/list/', CompanyView.as_view(), name='company_list'),
    path('company/create/', CompanyCreate.as_view(), name='company_create'),
    path('company/<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    # Company Advertisement end points
    path('ad/list/', AdView.as_view(), name='ad_list'),
    path('ad/create/', AdCreate.as_view(), name='ad_create'),
    path('ad/<int:pk>/', AdDetail.as_view(), name='ad_detail'),
]