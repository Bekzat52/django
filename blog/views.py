from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post

@api_view(['GET'])
def posts_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many = True)
    return Response(serializer.data)