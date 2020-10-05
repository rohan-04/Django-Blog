
from django.conf.urls import url
from . import views                             # . means current or same directory

app_name='articles'

urlpatterns = [
    url(r'^$',views.article_list, name = "list"),         # ^ means start and $ means end
    url(r'^create/$', views.article_create, name = "create"),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name = "detail"),  
]
