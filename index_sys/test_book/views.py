from django.shortcuts import render
from django.http import HttpResponse
from .models import books
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'test_book/index.html',{'content':'hi python'})

def test(request):
    return HttpResponse("this is a test")

def show_books(request):
    book_list = books.objects.all()
    return render(request,'test_book/show_books.html',{'books':book_list})

    
def show_json(request):
    json = {
        "SearchName":'被搜索的名字',
        "categories" : ['衣服','裤子','鞋子','帽子','背包','被子','床单'],
        "data":[100,200,300,110,1000,800,20]
    }
    return JsonResponse(json,safe=False)
    # return render(request,{})

