from django.shortcuts import render
import datetime
year = datetime.datetime.now().year

# Add the following import
from django.http import HttpResponse

# Our Models
from .models import Dog
# from dog_class.py import Dog

# Create your views here.
# Define the home view
def home(request):
  return render(request, 'home.html')
#   return HttpResponse('<h1>Hello</h1>')

# Define the about view
def about(request):
  context = { 'year': year }
  return render(request, 'about.html', context) # The 'render' function will look exclusively in the 'templates' folder for the templates
#   return HttpResponse('<h1>About the Dog Collector</h1>')

# Define the 'about/' view
def dogs_index(request):
    dogs = Dog.objects.all()
    context = { 'dogs': dogs } # context is used for future growth
    print('dogs dogs dogs dogs dogs dogs dogs dogs')
    print(dogs)
    return render(request, 'dogs/index.html', context)