from rest_framework import serializers
from .models import Category, Product, Book


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=("id","title")


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Product
        fields=("url","product_tag","name","category","stock","price","imageUrl","status","date_created")

class BookSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model=Book
        fields=("url","title","category","isbn","pages","price","stock","description","imageUrl","status","date_created")