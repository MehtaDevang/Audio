from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'audioApp'
urlpatterns = [
    url(r'create_audio/', views.create_audio, name='create_audio'),
    path('delete_audio/<str:audioFileType>/<int:audioFileID>', views.delete_audio, name='delete_audio'),
    path('update_audio/<str:audioFileType>/<int:audioFileID>', views.update_audio, name='update_audio'),
    path('get_audio/<str:audioFileType>/<int:audioFileID>', views.get_audio, name='get_audio'),
    path('get_audio/<str:audioFileType>', views.get_audio, name='get_audio'),
]