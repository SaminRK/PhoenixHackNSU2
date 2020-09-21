from django.shortcuts import render
from django.http import HttpResponse
 
from products.models import Product
from tenders.models import Tender, TenderBid

# Create your views here.
def index(request):
    organisations_list = Product.objects.all()
    context = {'products_list': products_list}
    return render(request, 'organisations/index.html', context)

def detail(request, product_id):
    # if insider user
    try:
        organisation = Organisation.objects.get(pk=organisation_id)
    except Organisation.DoesNotExist:
        raise Http404("Organisation Not Found")
    userOrganisation = UserOrganisation.objects.filter(user_id=request.user.id)
    if userOrganisation.filter(organisation=organisation).exists():
        products = Product.objects.filter(owner=organisation_id)
        issuedTenders = Tender.objects.filter(issuerOrganisation=organisation_id)
        tenderBids = TenderBid.objects.filter(bidderOrganisation=organisation_id)
        return render(request, 
            'organisations/insider_detail.html', {
                'organisation' : organisation,
                'products_list' : products ,
                'issued_tenders' : issuedTenders,
                'bidded_tenders' : tenderBids,
            })
    products_for_sale = Product.objects.filter(owner=organisation_id).filter(isForSale=True)
    return render(request, 
            'organisations/detail.html', {
                'organisation' : organisation,
                'products_list' : products_for_sale ,
            })

def order(request, product_id, organisation_id):
    # if insider user
    try:
        organisation = Organisation.objects.get(pk=organisation_id)
    except Organisation.DoesNotExist:
        raise Http404("Organisation Not Found")
    userOrganisation = UserOrganisation.objects.filter(user_id=request.user.id)
    if userOrganisation.filter(organisation=organisation).exists():
        products = Product.objects.filter(owner=organisation_id)
        issuedTenders = Tender.objects.filter(issuerOrganisation=organisation_id)
        tenderBids = TenderBid.objects.filter(bidderOrganisation=organisation_id)
        return render(request, 
            'organisations/insider_detail.html', {
                'organisation' : organisation,
                'products_list' : products ,
                'issued_tenders' : issuedTenders,
                'bidded_tenders' : tenderBids,
            })
    products_for_sale = Product.objects.filter(owner=organisation_id).filter(isForSale=True)
    return render(request, 
            'organisations/detail.html', {
                'organisation' : organisation,
                'products_list' : products_for_sale ,
            })