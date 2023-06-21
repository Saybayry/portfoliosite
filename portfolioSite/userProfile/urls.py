from django.urls import path, include
from . import views
app_name = "userProfile"
urlpatterns = [
    path('',include('django.contrib.auth.urls'), name="users"),
    path('register/', views.register, name ="register"),
    path('logoutt/', views.logoutt, name ="logoutt"),
    path('profile/', views.profile, name ="profile"),
]