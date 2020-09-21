from django.shortcuts import render
from django.http import HttpResponse

from .models import Organisation, UserOrganisation
from products.models import Product, Order, Inventory
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
    except Organisation.DoesNotExist:
        raise Http404("Organisation Not Found")
    userOrganisation = UserOrganisation.objects.filter(user_id=request.user.id)
    if userOrganisation.filter(organisation=organisation).exists():
        products = Inventory.objects.filter(organisation=organisation).values(
            'product',
            'product__name',
            'product__description',
            'quantity',
            'unit',
            'isForSale',
        )
        issuedTenders = Tender.objects.filter(issuerOrganisation=organisation_id)
        tenderBids = TenderBid.objects.filter(bidderOrganisation=organisation_id)
        orders_for = Order.objects.filter(toOrganisation=organisation).values(
            'fromOrganisation',
            'fromOrganisation__name',
            'product',
            'product__name',
            'quantity',
            'unit',
            'orderPlacedAt'
        )
        return render(request, 
            'organisations/insider_detail.html', {
                'organisation' : organisation,
                'products_list' : products ,
                'issued_tenders' : issuedTenders,
                'bidded_tenders' : tenderBids,
                'orders_for' : orders_for,
            })
    products_for_sale = Inventory.objects.filter(organisation=organisation).filter(isForSale=True).values(
        'product',
        'product__name',
        'product__description',
        'quantity',
        'unit',
        'isForSale',    
    )
    return render(request, 
            'organisations/detail.html', {
                'organisation' : organisation,
                'products_list' : products_for_sale ,
            })
    