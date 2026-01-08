from django.urls import path
from users.views import dashboard, service_detail, contact_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('service/<int:service_id>/', service_detail, name="service_detail"),
    path('contact/', contact_view, name="contact"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

