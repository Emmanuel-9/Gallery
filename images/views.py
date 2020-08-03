from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
def home(request):
    return render(request,'index.html')

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term) 
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": searched_images})

    else:
        message = "You have not searched for any term"
        return render(request, 'search.html',{"message": message})    

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404
       
    return render(request,"images.html", {"image":image})        