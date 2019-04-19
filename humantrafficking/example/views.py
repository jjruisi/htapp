from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from example.search import Search
from example.db import dbinsert

class HomePageView(TemplateView):
    template_name = "index.html"

@csrf_exempt
def test_ajax(request):
    if request.method == "POST":

        # get data from ajax post
        keywords = request.POST.get('keywords')
        location = request.POST.get('location')
        lang = request.POST.get('lang')
        
        #split up keyword string into list
        searchterms = keywords.split(',')

        #search
        newSearch = Search(searchterms, lang, location)
        array = newSearch.searchloop()
        dbinsert(array, location, lang)

        # data to return to the view
        data = {
            'data' : keywords
        }

    return JsonResponse(data)

