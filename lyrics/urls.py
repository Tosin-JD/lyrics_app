from django.urls import path
from . import views

app_name = "lyrics"


urlpatterns = [
       path('', views.LyricList.as_view(), name='all'),
       path('add/', views.CreateLyric.as_view(), name='add'),
       path('complete/<slug>/', views.SecondCreateLyric.as_view(), name='complete'),
       path('delete/<slug>/', views.DeleteLyric.as_view(), name='delete'),
       path('single/<slug>/', views.LyricDetail.as_view(), name="single"),
       path('json-api/', views.lyric_json, name="json"),

       path('add-chorus/to/<slug>/', views.CreateChorus.as_view(), name='add-chorus'),
       path('add-verse/to/<slug>/', views.CreateVerse.as_view(), name='add-verse'),
       path('add-bridge/to/<slug>/', views.CreateBridge.as_view(), name='add-bridge'),

       path('edit-chorus/to/<int:pk>/', views.UpdateChorus.as_view(), name='edit-chorus'),
       path('edit-verse/to/<int:pk>/', views.UpdateVerse.as_view(), name='edit-verse'),
       path('edit-bridge/to/<int:pk>/', views.UpdateBridge.as_view(), name='edit-bridge'),

       path('delete-chorus/to/<int:pk>/', views.DeleteChorus.as_view(), name='delete-chorus'),
       path('delete-verse/to/<int:pk>/', views.DeleteVerse.as_view(), name='delete-verse'),
       path('delete-bridge/to/<int:pk>/', views.DeleteBridge.as_view(), name='delete-bridge'),
              
    ]  
    






