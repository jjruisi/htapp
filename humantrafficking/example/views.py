from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from example.search import Search

class HomePageView(TemplateView):
    template_name = "index.html"

@csrf_exempt
def test_ajax(request):
    if request.method == "POST":

        # get data from ajax post
        string = request.POST.get('data')

        # do search stuff here
        searchterms = []
        searchterms.append('bad')

        newSearch = Search(searchterms, 'com', 'g147288')
        newSearch.searchloop()

        # data to return to the view
        data = {
            'data' : string
        }

    return JsonResponse(data)

