from django.urls import path
from . import views

app_name = "lyrics"


urlpatterns = [
       path('', views.LyricList.as_view(), name='all'),
       path('add/', views.CreateLyric.as_view(), name='add'),
       path('complete/<slug>/', views.SecondCreateLyric.as_view(), name='complete'),
       path('delete/<slug>/', views.DeleteLyric.as_view(), name='delete'),
       path('single/<slug>/', views.LyricDetail.as_view(), name="single"),
       path('lyric-json/', views.lyric_json, name="json"),
    ]  
    






