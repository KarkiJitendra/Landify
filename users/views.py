from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from mainapp.models import HeroSection, AboutSection, Service, Stacks, FAQ, TeamMember, CompanyInfo, ContactMessage, FooterLink,PageBanner,Partner


def dashboard(requests):
    context = {
        'hero': HeroSection.objects.get(id=2),
        'about': AboutSection.objects.get(id=1),
        'service': Service.objects.all(),
        'stacks': Stacks.objects.all(),
        'team': TeamMember.objects.all(),
        'company': CompanyInfo.objects.all(),
        'faq': FAQ.objects.all(),
        'partner': Partner.objects.all(),
        'footerlink': FooterLink.objects.all(),
        'contact': ContactMessage.objects.all(),
        'pagebanner': PageBanner.objects.all()
    }
    return render(requests,'main/index.html', {'context':context})
