from django.shortcuts import render
from django.http import HttpResponse
from cr_note.models import Crn
from station.models import Station
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def index(request):

    return render(request, 'pages/index.html')

@login_required
def latest(request):
    #hapa chini tunataka listings 3 ambazo ni latest na published
    crns = Crn.objects.order_by('-created_at')[:100]

    context = {
        'crns': crns ,
    }
    return render(request, 'pages/latest.html' ,context)
