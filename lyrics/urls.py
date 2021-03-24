from django.urls import path
from . import views

app_name = "lyrics"


urlpatterns = [
       path('', views.LyricList.as_view(), name='list'),
       path('add/', views.CreateLyric.as_view(), name='add'),
       path('delete/<slug>/', views.DeleteLyric.as_view(), name='delete'),
       path('single/<slug>/', views.LyricDetail.as_view(), name="details"),
       path('lyric-json/', views.lyric_json, name="json"),
    ]  
    






