from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer, ActionSerializer
from .models import Moviedata
from django.core.paginator import Paginator
from fuzzywuzzy import fuzz

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='comedy')
    serializer_class = MovieSerializer

# def list_movie(request):
#     movies = Moviedata.objects.all()

#     #search
#     search_name = request.GET.get('search_movie_name')

#     if search_name !='' and search_name is not None:
#         movies = movies.filter(name = search_name)

#     #paginator
#     page_list = Paginator(movies, 10) # we need to get the page no from the request
#     page_no = request.GET.get('page')
#     movie_objects = page_list.get_page(page_no)


#     return render(request, 'Movie_API/list.html', {'movie_list': movie_objects})

def list_movie(request):
    search_name = request.GET.get('search_movie_name')
    movies = Moviedata.objects.all()

    if search_name:
        matches = movies.filter(name__icontains=search_name) # use icontains - this logic provides matching names not empty values

        if not matches.exists():
            matched_movies = []
            for movie in movies:
                ratio = fuzz.partial_ratio(search_name.lower(), movie.name.lower())
                if ratio > 70:
                    matched_movies.append(movie)
            matches = matched_movies
        
        movies = matches if isinstance(matches, list) else matches

    page_list = Paginator(movies, 10)
    page_no = request.GET.get('page')
    movie_objects = page_list.get_page(page_no)

    return render(request, 'Movie_API/list.html', {
        'movie_list': movie_objects,
        'search_query': search_name
    })