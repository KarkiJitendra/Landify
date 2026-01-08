from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from mainapp.models import HeroSection, AboutSection, Service, Stacks, FAQ, TeamMember, CompanyInfo, ContactMessage, FooterLink,PageBanner,Partner
from django.core.mail import send_mail
from django.contrib import messages

def dashboard(request):
    context = {
        'hero': HeroSection.objects.get(id=2),
        'about': AboutSection.objects.get(id=1),
        'serve': Service.objects.all(),
        'stacks': Stacks.objects.all(),
        'team': TeamMember.objects.all(),
        'company': CompanyInfo.objects.get(id=1),
        'faq': FAQ.objects.all(),
        'partner': Partner.objects.all(),
        'footerlink': FooterLink.objects.all(),
        'contact': ContactMessage.objects.all(),
        'pagebanner': PageBanner.objects.all()
    }
    return render(request,'main/index.html', context)

def service_detail(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        raise Http404("Service does not exist")
    other_services = Service.objects.exclude(id=service_id)
    context = {
        'service': service,
        'allservice': other_services,
        'company': CompanyInfo.objects.get(id=1),
        'pagebanner': PageBanner.objects.all()
    }
    return render(request, 'main/service.html', context)

def contact_view(request):
    sent = False
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            send_mail(
                subject,
                message,
                email,
                ['sabrejiten9761@gmail.com'],
                fail_silently=False,
            )
            sent = True
            messages.success(request, 'Thank you, mail sent!')
        except Exception as e:
            messages.error(request, 'Sorry – message could not be sent.')
        # return render(request, 'main/index.html', {'sent': True})
        return HttpResponse("Thank you, your message has been sent.")
        
    return render(request, 'main/index.html', {'sent': sent})

