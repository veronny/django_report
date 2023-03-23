from django.contrib import admin
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('rpt_padron/', include('rpt_padron.urls', namespace='rpt_padron')),
    
]
