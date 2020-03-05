from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="blog-home"),
    path('about/', views.about,name="blog-about"),
    path('detection/', views.detection,name="blog-detection"),
    path('dashboard/',views.dashboard,name="blog-dashboard"),
    path('chartpage/<str:username>/',views.chartpage,name="blog-chartpage"),
    
    #path('chartpage/<str:username>/', views.chartview,name='blog_chartview'),
    
    
    #books_views.BookDeleteView.as_view()
]