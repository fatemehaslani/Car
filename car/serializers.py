from datetime import datetime as dt
from rest_framework import serializers
from car.models import Category, Car


# from mysite.car.models import Category, Car


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class CarSerializer(serializers.ModelSerializer):
  #  tags_count = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Car
        # fields = '__all__'
        fields = ['id', 'car_name', 'description', 'model_car', 'color', 'category', 'tags']

    # car_name = serializers.CharField(max_length=200)
    # description = serializers.CharField(max_length=1024)
    # model_car = serializers.CharField(max_length=250)
    # color = serializers.CharField(max_length=200)
    # category = CategorySerializer()

   # def get_tags_count(self, obj: Car):
      #  return obj.tags_count()

    def create(self, validated_data):
        validated_data['published_date'] = dt.now()
        return super().create(validated_data)

    # id = serializers.IntegerField()

    # category = serializers.PrimaryKeyRelatedField(
    #   queryset=Category.objects.all(),
    #  serializer=CategorySerializer(),
# )
