from mainapp.models import FAQ, ContactMessage, TeamMember, SEOSettings, Stacks, HeroSection, AboutSection, Partner, Service
from django.utils.text import slugify
from django import http
from django.shortcuts import render, redirect


def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

def hero_section_admin(request):
    hero_sections = HeroSection.objects.all()
    return render(request, 'admin/templates/admin/hero_section.html', {'hero_sections': hero_sections})

def hero_section_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        primary_button_text = request.POST.get('primary_button_text')
        primary_button_link = request.POST.get('primary_button_link')
        secondary_button_text = request.POST.get('secondary_button_text')
        secondary_button_link = request.POST.get('secondary_button_link')
        hero_image = request.FILES.get('hero_image')
        is_active = bool(request.POST.get('is_active'))

        HeroSection.objects.create(
            title=title,
            subtitle=subtitle,
            description=description,
            primary_button_text=primary_button_text,
            primary_button_link=primary_button_link,
            secondary_button_text=secondary_button_text,
            secondary_button_link=secondary_button_link,
            hero_image=hero_image,
            is_active=is_active
        )
        return redirect('hero_section_admin')

    return render(request, 'admin/templates/admin/hero_section_add.html')

def hero_section_edit(request, hero_id):
    hero_section = HeroSection.objects.get(id=hero_id)

    if request.method == 'POST':
        hero_section.title = request.POST.get('title')
        hero_section.subtitle = request.POST.get('subtitle')
        hero_section.description = request.POST.get('description')
        hero_section.primary_button_text = request.POST.get('primary_button_text')
        hero_section.primary_button_link = request.POST.get('primary_button_link')
        hero_section.secondary_button_text = request.POST.get('secondary_button_text')
        hero_section.secondary_button_link = request.POST.get('secondary_button_link')
        
        if 'hero_image' in request.FILES:
            hero_section.hero_image = request.FILES.get('hero_image')
        
        hero_section.is_active = bool(request.POST.get('is_active'))
        hero_section.save()
        return redirect('hero_section_admin')

    return render(request, 'admin/templates/admin/hero_section_edit.html', {'hero_section': hero_section})


