from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="blog-home"),
    path('about/', views.about,name="blog-about"),
    path('detection/', views.detection,name="blog-detection"),
    path('howday/', views.howday,name="blog-howday"),
    path('dashboard/',views.dashboard,name="blog-dashboard"),
    path('chartpage/<slug:user_id>/',views.chartpage,name="blog-chartpage"),
    
    #path('chartpage/<str:username>/', views.chartview,name='blog_chartview'),
    
    
    #books_views.BookDeleteView.as_view()
]