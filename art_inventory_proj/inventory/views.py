from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the inventory index.")

def detail(request, artist_id):
    return HttpResponse("You're looking at the details of piece %s." % artist_id)

