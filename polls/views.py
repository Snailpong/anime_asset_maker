from django.shortcuts import render
from django.http import HttpResponse

def background(request):
    return render(request, 'anime_asset/background.html')

def mesh(request):
    return render(request, 'anime_asset/mesh.html')

def mixamo(request):
    return render(request, 'anime_asset/mixamo.html')

def blender(request):
    return render(request, 'anime_asset/blender.html')