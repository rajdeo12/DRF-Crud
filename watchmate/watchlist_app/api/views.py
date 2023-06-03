from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializer import WatchListserializer,StreamPlatformserializer,Reviewseri
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
 

# class ReviewCreate(generics.CreateAPIView):
#     #queryset=Review.objects.all()
#     serializer_class=Reviewseri
#     permission_classes=[IsAuthenticated]

#     def perform_create(self,serializer):
#         pk=self.kwargs.get("pk")
#         Watchlist=WatchList.objects.get(pk=pk)
#         serializer.save(WatchList=Watchlist)

class ReviewCreate(generics.CreateAPIView):
    serializer_class=Reviewseri

    def perform_create(self, serializer):
        pk=self.kwargs.get("pk")
        watchlist=WatchList.objects.get(pk=pk)

        serializer.save(WatchList=watchlist)

        

class Reviewlist(generics.ListAPIView):
   # queryset=Review.objects.all()
    serializer_class=Reviewseri

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    
    
class ReviewDetail(generics.RetrieveUpdateAPIView):
    queryset=Review.objects.all()
    serializer_class=Reviewseri
    #permission_classes=[Review]

   


class StreamplatformAV(APIView):
    
    def get(self,request):
        watchlist=StreamPlatform.objects.all()
        seri=StreamPlatformserializer(watchlist,many=True)
        return Response(seri.data)
    
    def post(self,request):
        seri=StreamPlatformserializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        else:
            return Response(seri.data,status=status.HTTP_404_NOT_FOUND)

class StreamplatformDetailAV(APIView):
    
    def get(self,request,pk):
        st=StreamPlatform.objects.get(pk=pk)
        seri=StreamPlatformserializer(st)
        return Response(seri.data)

    def put(self,request,pk):
        st=StreamPlatform.objects.get(pk=pk)
        seri=StreamPlatformserializer(st,data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        else:
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        st=StreamPlatform.objects.get(pk=pk)
        st.delete()
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
class WatchListAV(APIView):
    
    def get(self,request):
        movie=WatchList.objects.all()
        seri=WatchListserializer(movie,many=True)
        return Response(seri.data)
        
    def post(self,request):
        seri=WatchListserializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        else:
            return Response(seri.errors)

class WatchlistDetailAV(APIView):
    
    def get(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        seri=WatchListserializer(movie)
        return Response(seri.data)
    
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        seri=WatchListserializer(movie,data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        else:
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


# @api_view(["GET","POST"])
# def movielist(request):
#     if request.method=="GET":
#         movie=Movie.objects.all()
#         seri=Movieserializer(movie,many=True)
#         return Response(seri.data)
    
#     if request.method=="POST":
#         seri=Movieserializer(data=request.data)
#         if seri.is_valid():
#             seri.save()
#             return Response(seri.data)
#         else:
#             Response(seri.errors)
    
    
# @api_view(["GET","PUT"])
# def movie_detail(request,pk):
#     if request.method=="GET":
#         movie=Movie.objects.get(pk=pk)
#         seri=Movieserializer(movie)
#         return Response(seri.data)

#     if request.method=="PUT":
#         movie=Movie.objects.get(pk=pk)
#         seri=Movieserializer(movie,data=request.data)
#         if seri.is_valid():
#             seri.save()
#             return Response(seri.data)
#         else:
#             Response(seri.errors)