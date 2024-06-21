from rest_framework import serializers
from .models import *
from account.serializers import AgencySerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
   
        
class TourSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    agency = AgencySerializer()
    class Meta:
        model = Tour
        fields = '__all__'
        
    def create(self, validated_data):
        categories_data = validated_data.pop('category')
        agency_data = validated_data.pop('agency')
        agency, created = Agency.objects.get_or_create(**agency_data)
        tour = Tour.objects.create(agency=agency, **validated_data)
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(**category_data)
            tour.category.add(category)
        return tour
    

class TourServiceSerializer(serializers.ModelSerializer):
    # tour = serializers.PrimaryKeyRelatedField(queryset=Tour.objects.all())
    class Meta:
        model = TourService
        fields = '__all__'
  
        
class MeadiTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaTour
        fields = '__all__'
 
         
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'