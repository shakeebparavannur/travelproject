from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.
def home(request):


    obj=Place.objects.all()
    teams=Team.objects.all()

    return render(request,"index.html",{'res':obj,'team':teams})