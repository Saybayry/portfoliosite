from django.urls import path
from .views import index, album,autors
app_name = 'portfolio'

urlpatterns = [
    path('', index, name= 'index'),
    path('autor/', autors, name= 'autor'),
    path('album/', album, name= 'album'),

]
