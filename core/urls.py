from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blogs'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('repositaries/', views.repositaries, name='repositaries'),
    path('project/',views.project,name='projects'),
    path('project/<slug:slug>/',views.project_detail,name='project_detail'),
    path('searchblogs/', views.searchblogs, name='searchblogs'),
    path('searchprojects/', views.searchprojects, name='searchprojects'),
    path('contact/', views.contact, name='contact'),
  
]