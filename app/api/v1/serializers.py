from rest_framework import generics
from rest_framework import serializers

from app.models import Category, Comments, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category', 'is_published']


class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'category', 'is_published']


class BlogDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['text']
