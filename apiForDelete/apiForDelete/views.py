from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    products=[
        'Lays',
        'Parle-G',
        'Nissin'
    ]
    return JsonResponse(products,safe=False)