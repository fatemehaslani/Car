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
    file_address = serializers.SerializerMethodField(method_name='file_address_field')


    class Meta:
        model = Car
        # fields = '__all__'
        fields = ['id', 'car_name', 'description', 'model_car', 'color', 'category', 'tags', 'file_address']

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


    def file_address_field(self, obj: Car):
        if obj.file:
            return "http://127.0.0.1:8000" + obj.file.url
        return ''

    # id = serializers.IntegerField()

    # category = serializers.PrimaryKeyRelatedField(
    #   queryset=Category.objects.all(),
    #  serializer=CategorySerializer(),
# )
