from django.conf.urls import include,url
from . import views
urlpatterns = [
    url(r'^index$',views.index),
    url(r'^test',views.test),
    url(r'^show$',views.show_books),
    url(r'^show_json',views.show_json)
]