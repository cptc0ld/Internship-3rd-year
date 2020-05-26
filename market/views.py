from django.shortcuts import render
from . import models
# Create your views here.

def market(request):
    cat = models.Category.objects.all()
    print(cat)
    return render(request, 'market.html', {'cat': cat})