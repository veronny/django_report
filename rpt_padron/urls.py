from django.urls import path
from .views import Rpt_padron

app_name = "rpt_padron"

urlpatterns = [
    path('',Rpt_padron.as_view(),name='home')
]
