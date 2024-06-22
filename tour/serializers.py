from rest_framework import serializers
from .models import *
from account.serializers import AgencySerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
   

class MeadiTourListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaTour
        exclude = ['tour']
 

class TourSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    media = MeadiTourListSerializer()
    class Meta:
        model = Tour
        fields = '__all__'
        
    def create(self, validated_data):
        categories_data = validated_data.pop('category')
        medias = validated_data.pop('media')
        agency_data = validated_data.pop('agency')
        agency, created = Agency.objects.get_or_create(**agency_data)
        tour = Tour.objects.create(agency=agency, **validated_data)
        
        media_serializer = MeadiTourListSerializer(data=medias, many=True)
        media_serializer.is_valid(raise_exception=True)
        media_serializer.save()
        
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(**category_data)
            tour.category.add(category)
        return tour
    

class TourListSerializer(serializers.ModelSerializer):
    media = serializers.SerializerField()
    class Meta:
        model = Tour
        fields = '__all__'

    def get_media(self, obj):
        return MeadiTourListSerializer(obj.media.all(), many=True).data
     


class TourServiceSerializer(serializers.ModelSerializer):
    # tour = serializers.PrimaryKeyRelatedField(queryset=Tour.objects.all())
    class Meta:
        model = TourService
        fields = '__all__'
  
        
         
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
