from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
year = datetime.datetime.now().year

# Add the following import
from django.http import HttpResponse

# Our Models
from .models import Dog
from .models import Toy
# from .dog_class import dogs
# from dog_class.py import Dog

# Create your views here.
# Define the home view
def home(request):
  return render(request, 'home.html')
#   return HttpResponse('<h1>Hello</h1>')

# Define the about view
def about(request):
#   context = { 'year': year }
  return render(request, 'about.html') # The 'render' function will look exclusively in the 'templates' folder for the templates
# return render(request, 'about.html', context)
#   return HttpResponse('<h1>About the Dog Collector</h1>')

# Define the 'dogs/' view
def dogs_index(request):
    dogs = Dog.objects.order_by('id')
    context = { 'dogs': dogs } # context is used for future growth
    print('dogs dogs dogs dogs dogs dogs dogs dogs')
    print(dogs)
    return render(request, 'dogs/index.html', context)

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', { 'dog': dog })

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'
#   fields = ['name', 'breed', 'description', 'age'] # This is the same as above

class DogUpdate(UpdateView):
  model = Dog
  # Let's disallow the renaming of a dog by excluding the name field!
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

# Define the 'toys/' view
def toys_index(request):
    toys = Toy.objects.order_by('id')
    context = { 'toys': toys } # context is used for future growth
    print('toys toys toys toys toys toys toys toys')
    print(toys)
    return render(request, 'toys/index.html', context)

def toys_detail(request, toy_id):
    toy = Toy.objects.get(id=toy_id)
    return render(request, 'toys/detail.html', { 'toy': toy })

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'
#   fields = ['name', 'color'] # This is the same as above

class ToyUpdate(UpdateView):
  model = Toy
  # Let's disallow the renaming of a toy by excluding the name field!
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'
