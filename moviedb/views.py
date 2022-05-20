from django.shortcuts import render, redirect
from .utils import searchMovie
import requests

api_key = 'e70b4a00'

def movieDb(request):
    search_query = searchMovie(request)
    response = requests.get('http://www.omdbapi.com/?s='+ search_query +'&apikey='+api_key)
    data = response.json()
    context = {'data': data}
    return render(request, 'moviedb/moviedb.html', context)

def selectedMovie(request, pk):
    response = requests.get('http://www.omdbapi.com/?i='+ pk +'&plot=full&apikey='+api_key)
    data = response.json()
    context = {'data': data}
    return render(request, 'moviedb/selectedmovie.html', context)

def savedMovies(request):
    # response = requests.get('http://www.omdbapi.com/?i='+ pk +'&plot=full&apikey='+api_key)
    # data = response.json()
    return render(request, 'moviedb/savedmovies.html')