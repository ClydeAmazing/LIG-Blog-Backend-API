from rest_framework import viewsets, pagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param, remove_query_param
from api.models import Post, Comment
from api.serializers import PostSerializer

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        
        base_url = self.request.build_absolute_uri()
        return Response({
            'data': data,
            'links': {
                'first': remove_query_param(base_url, self.page_query_param),
                'last': replace_query_param(base_url, self.page_query_param, self.page.paginator.num_pages),
                'prev': self.get_previous_link(),
                'next': self.get_next_link()
            },
            'meta': {
                'current_page': self.page.number,
                'last_page': self.page.paginator.num_pages,
                'path': remove_query_param(base_url, self.page_query_param),
                'per_page': self.page_size,
                'total': self.page.paginator.num_pages,
            }
        })

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'data': serializer.data})


    
    