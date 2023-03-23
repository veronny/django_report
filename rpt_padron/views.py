from django.shortcuts import render
from django.views.generic import View
# report excel
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill,Side

# Create your views here.
class Rpt_padron(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request,'rpt_padron.html',context)