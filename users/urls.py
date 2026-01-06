from django.urls import path
from users.views import dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
