from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'main_site/index.html')

def aboutme(request):
    return render(request, 'main_site/aboutme.html')

def bubble_sort(request):
    return render(request, 'main_site/bubblesort.html')

def selection_sort(request):
    return render(request, 'main_site/selectionsort.html')

def quick_sort(request):
    return render(request, 'main_site/quicksort.html')

def merge_sort(request):
    return render(request, 'main_site/mergesort.html')

def insertion_sort(request):
    return render(request, 'main_site/insertionsort.html')