from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def my_index(request):
    return render(request,'my_index/index.html')


def search_json(request):
    json = {
        "source_type":['pc','mobile'],
        "pc":[120, 132, 101, 134, 90, 230, 210],
        "mobile":[220, 182, 191, 234, 290, 330, 310]
    } 
    return JsonResponse(json)