from django.shortcuts import render
from .models import Batch, Doner 

# Create your views here.

def index(request):
    a = Batch.objects.all
    b = Doner.objects.all
    return render(request, "index.html",{'a':a, 'b':b})
    