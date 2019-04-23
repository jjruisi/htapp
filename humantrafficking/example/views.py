from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from example.search import Search
from example.search2 import Search
from example.db import dbinsert
import json

class HomePageView(TemplateView):
    template_name = "index.html"

@csrf_exempt
def test_ajax(request):
    if request.method == "POST":

        # get data from ajax post
        keywords = request.POST.get('keywords')
        location = request.POST.get('location')
        lang = request.POST.get('lang')
        
        # split up keyword string into list
        searchterms = keywords.split(',')

        # search
        newSearch = Search(searchterms, lang, location)
        array = newSearch.searchloop()

        # insert search result into db
        dbinsert(array, location, lang)

        # convert array to json
        arr = []
        for review in array:
            x = [review[0], review[1]]
            arr.append(x)
        # data to return to the view
        data = {
            "data" : arr
        }

        jsonlist = json.dumps(data)

    return JsonResponse(jsonlist, safe=False)

