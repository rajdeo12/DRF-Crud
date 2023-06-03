
from rest_framework import serializers
from watchlist_app.models import  StreamPlatform,WatchList,Review

class Reviewseri(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
         model=Review
         exclude=('watchlist',)
         #fields='__all__'
         
class WatchListserializer(serializers.ModelSerializer):
    review=Reviewseri(many=True,read_only=True)
    
    class  Meta:
         model=WatchList
         fields="__all__"

class StreamPlatformserializer(serializers.ModelSerializer):
    WatchList=WatchListserializer(many=True,read_only=True)
    
    class Meta:
         model=StreamPlatform
         fields="__all__"
   
   #this is used only in serializer not in modelserializser 
    # def create(self,validated_data):
    #     return Movie.objects.create(**validated_data)
        
    # def update(self,instance,validated_data):
    #     instance.name=validated_data.get("name",instance.name)  
    #     instance.discripstion=validated_data.get("name",instance.discripstion)  
    #     instance.active=validated_data.get("name",instance.active)
    #     instance.save()
    #     return instance  