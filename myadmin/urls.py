from django.urls import path
from .views import admin_dashboard, hero_section_admin, hero_section_add, hero_section_edit
from mainapp.models import HeroSection

urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),  
    
]