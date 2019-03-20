from django.conf.urls import include,url
from . import views
urlpatterns = [
    url(r'^my_index$',views.my_index),
    url(r'^search_json$',views.search_json),

]