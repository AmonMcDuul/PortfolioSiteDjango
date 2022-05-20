from django.db.models import Q

def searchMovie(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    return search_query