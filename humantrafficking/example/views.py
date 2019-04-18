from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class HomePageView(TemplateView):
    template_name = "index.html"

@csrf_exempt
def test_ajax(request):
    if request.method == "POST":
        string = request.POST.get('data')
        data = {
            'data' : string
        }
    return JsonResponse(data)

