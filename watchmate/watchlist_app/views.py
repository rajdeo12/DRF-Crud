# from django.shortcuts import render
# from . models import *
# from django.http import JsonResponse

# def movie_list(request):
#     movie=Movie.objects.all()
#     data = {
#         "movies": tuple(movie.values())
#     }
#     return JsonResponse(data)

# def movie_detail(request,pk):
#     movie=Movie.objects.get(pk=pk)
#     data={
#         "name": movie.name,
#         "description": movie.discription,
#         "active": movie.active,
#          }
#     return JsonResponse(data)
