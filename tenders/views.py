from django.shortcuts import render
from django.http import HttpResponse

from .models import Tender, TenderBid
from products.models import ProductsInProductList
from organisations.models import Organisation

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

def newTender(request, organisation_id):
    
    if request.method != "POST":
        # if user is from the organisation
        user = request.user
        organisation = Organisation.objects.get(pk=organisation_id)
        return render(request, 'tenders/new_tender_form.html', { 'user' : user, 'organisation' : organisation})
    else:
        # enter new tender into db
        productList = ProductList(description='product list for tender')
        productList.save()
        postedProductList = request.POST.get['products']
        for postedProduct in postedProductList:
            newProduct = Product(
                name=postedProduct.name,
                isForSale=False,
            )
            newProduct.save()
            productsInProductList = ProductsInProductList(
                productList=productList,
                product=newProduct,
                quantity=postedProduct.quantity,
                unit=postedProduct.unit,
            )
            productsInProductList.save()
        tender = Tender(
            issuerOrganisation=Organisation.objects.get(pk=organisation_id),
            productList=productList,
        )
        tender.save()

        return redirect('tenders/organisations/' + str(organisation_id))
