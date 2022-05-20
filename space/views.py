from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import PostComment
import requests

# nasa_api_key = 'VAiYtvqjs3nU8NEbBDLuVfSpWv8FXZH5ZASw4tDG'

def spaceNews(request):
    response = requests.get('https://api.spaceflightnewsapi.net/v3/articles')
    data = response.json()
    context = {'data': data}
    return render(request, 'space/spacenews.html', context)

def apod(request):
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=VAiYtvqjs3nU8NEbBDLuVfSpWv8FXZH5ZASw4tDG')
    data = response.json()
    context = {'data': data}
    return render(request, 'space/apod.html', context)

def marsPost(request):
    response = requests.get('https://api.spaceflightnewsapi.net/v3/articles?_limit=10&_title_contains=mars')
    data = response.json()
    context = {'data': data}
    return render(request, 'space/marspost.html', context)

def singlePage(request, pk):
    response = requests.get('https://api.spaceflightnewsapi.net/v3/articles?id='+ pk)
    data = response.json()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.source_id = pk
        comment.save()
    commentsObj = PostComment.objects.filter(source_id=pk)
    context = {'data': data, 'form': form, 'comments': commentsObj}
    return render(request, 'space/singlepage.html', context)