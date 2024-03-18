from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''

    return HttpResponse('Welcome to 6410742537 Setthanan Thitathanapat views!')

def item_view(request, item_id):

    context_data = {
        "item_id": item_id
    }
    return render(request, 'index.html',context= context_data)

def item_view1(request):

    return render(request, 'homepage.html')

def item_view2(request):

    return render(request, 'category.html')

def item_view3(request):

    return render(request, 'product.html')

def item_view4(request):

    return render(request, 'checkout.html')

def item_view5(request):

    return render(request, 'contact.html')

@csrf_exempt
def basic_request(requests):
    if requests.method == "GET":
        return JsonResponse({"status": "GET Pass"}, safe=False)

    if requests.method == "POST":
        return JsonResponse({"status": "POST Pass"}, safe=False)

