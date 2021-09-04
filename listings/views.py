from django.core import paginator
from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index(request): 
    listings = Listing.objects.all()

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = { "listings": page_listings}
    return render(request, 'listings/listings.html', context)
 
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/listing.html', {'listing': listing})

def search(request):
    return render(request, 'listings/search.html')
