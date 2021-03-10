from django.urls import path, re_path
from .views import register, activate, UserDetailView


urlpatterns = [
    path('register/', register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('detail/', UserDetailView.as_view(), name='user_detail'),

]