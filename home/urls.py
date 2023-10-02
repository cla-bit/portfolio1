from django.urls import path, re_path
from .views import HomeView, AboutView, ProjectView, ProjectDetailView, ContactView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about-me/', AboutView.as_view(), name='about_me'),
    path('projects/', ProjectView.as_view(), name='project_list'),
    path('projects/<slug:category_slug>/', ProjectView.as_view(), name='project_list_category'),
    path('detail/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]
