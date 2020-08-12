from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'Home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/', views.image, name = 'image'),
    url(r'^location/',views.location, name = 'Location'),
    url(r'^category/',views.category, name = 'category') 
    
   
]
if settings.DEBUG: 
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)