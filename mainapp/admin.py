from django.contrib import admin
from .models import HeroSection, AboutSection, Service, Stacks, PageBanner,Partner
# Register your models here.

admin.site.register(HeroSection)
admin.site.register(Service)
admin.site.register(AboutSection)
admin.site.register(Stacks)
admin.site.register(Partner)
    