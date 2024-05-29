from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'Lays',
        'Parle-G',
        'Nissin'
    ]
    return JsonResponse(friends,safe=False)