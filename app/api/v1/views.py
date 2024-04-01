from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes, action
from django.shortcuts import get_object_or_404
from rest_framework import status
from app.models import Category, Comments, Blog
from .serializers import CategorySerializer, BlogCreateSerializer, BlogUpdateSerializer, BlogSerializer, \
    CommentCreateSerializer
from rest_framework.views import APIView

from ...permissions import IsOwner


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]


@api_view(http_method_names=['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_blog(request):
    serializer = BlogCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(http_method_names=['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogUpdateSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(http_method_names=['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['POST'])
    def create_comment(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = CommentCreateSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class BlogUpdateAPIView(APIView):
    permission_classes = [IsOwner]
    authentication_classes = [TokenAuthentication]

    def put(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        self.check_object_permissions(self.request, blog)
        serializer = BlogUpdateSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)


class BlogDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Blog.objects.all()
