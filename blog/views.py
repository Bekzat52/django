from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .models import Post
from blog import serializers

@api_view(['GET'])
def posts_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    data = request.POST
    serializer = PostSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return  Response('Пост успешно создан')

@api_view(['GET'])
def post_detail(request, p_id):
    post = get_object_or_404(Post, id=p_id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['DELETE'])
def post_delete(request, p_id):
    post = get_object_or_404(Post, id=p_id)
    post.delete()
    return Response('Пост успешно удален')

@api_view(['PUTH', 'PATH'])
def post_update(request, p_id):
    post = get_object_or_404(Post, id=p_id)
    serializer = PostSerializer(post, request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Пост успешно обновлен')

