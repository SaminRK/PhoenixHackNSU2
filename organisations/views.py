from django.shortcuts import render
from django.http import HttpResponse

from .models import Organisation
from products.models import Product
from tenders.models import Tender, TenderBid

# Create your views here.
def index(request):
    organisations_list = Organisation.objects.all()
    context = {'organisations_list': organisations_list}
    return render(request, 'organisations/index.html', context)

def detail(request, organisation_id):
    # if insider user
    try:
        organisation = Organisation.objects.get(pk=organisation_id)
        products = Product.objects.filter(owner_id=organisation_id)
        issuedTenders = Tender.objects.filter(issuerOrganisation=organisation_id)
        tenderBids = TenderBid.objects.filter(bidderOrganisation=organisation_id)
    except Organisation.DoesNotExist:
        raise Http404("Organisation Not Found")
    return render(request, 
        'organisations/insider_detail.html', {
            'organisation' : organisation,
            'products_list' : products ,
            'issued_tenders' : issuedTenders,
            'bidded_tenders' : tenderBids,
        })
