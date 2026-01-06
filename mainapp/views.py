from django.shortcuts import render, redirect
from .models import HeroSection, AboutSection, Partner, Service, SEOSettings, Stacks
# from .form import Aboutform, Heroform

def homepage(request):
    return render(request, 'DigitalMarketing/templates/main/index.html')

def herosection(request):
    hero = HeroSection.objects.all()
    
      
    