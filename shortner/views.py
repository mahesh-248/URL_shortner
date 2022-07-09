from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
# function which renders the html file and dislays in web app
def index(request):
    return render(request, 'index.html')

# function to store the link and its corresponding shortened link in Data base
def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        link_id = str(uuid.uuid4())[:5]
        data_tuple = Url(link=link,uuid=link_id)
        data_tuple.save()
        return HttpResponse(link_id)

# function redirects to the url for given shortened url through database 
def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)