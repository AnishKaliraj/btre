from listings.views import listing
from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_pulished=True)[:3]
    return render(request, 'pages/index.html', {'listings': listings})

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')[:3]
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    return render(request, 'pages/about.html', {'realtors': realtors, 'mvp_realtors': mvp_realtors})
