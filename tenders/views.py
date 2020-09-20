from django.shortcuts import render
from django.http import HttpResponse

from .models import Tender, TenderBid
from products.models import ProductsInProductList

# Create your views here.
def index(request):
    return HttpResponse("Should view tender issued and bidded by my organisation")

def detail(request, tender_id):
    # if user is from issuing organisation
    try:
        tender = Tender.objects.get(pk=tender_id)
        products = ProductsInProductList.objects.filter(productList=tender.productList)
        tenderBids = TenderBid.objects.filter(tender=tender_id)
    except Tender.DoesNotExist:
        raise Http404("Tender Not Found")
    return render(request, 'tenders/issuer_detail.html', {
            'tender' : tender,
            'products' : products,
            'tender_bids' : tenderBids ,  
        })
