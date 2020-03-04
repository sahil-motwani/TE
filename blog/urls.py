from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="blog-home"),
    path('about/', views.about,name="blog-about"),
    path('detection/', views.detection,name="blog-detection"),
    path('dashboard/',views.dashboard,name="blog-dashboard"),

    
    #books_views.BookDeleteView.as_view()
]