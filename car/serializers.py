from rest_framework import serializers
from car.models import Category
from mysite.car.models import Car


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
    #id = serializers.IntegerField()
    #car_name = serializers.CharField(max_length=200)
    #description = serializers.CharField(max_length=1024)
    #model_car = serializers.CharField(max_length=250)
    #color = serializers.CharField(max_length=200)
    category = CategorySerializer()

    #category = serializers.PrimaryKeyRelatedField(
     #   queryset=Category.objects.all(),
      #  serializer=CategorySerializer(),
   # )