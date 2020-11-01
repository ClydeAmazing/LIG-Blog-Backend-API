from rest_framework import viewsets, pagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils.urls import replace_query_param, remove_query_param
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import mixins, status
from django.contrib.auth.models import User
from api.models import Post, Comment
from api.serializers import PostSerializer, CommentSerializer
import json

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

class BearerAuthentication(TokenAuthentication):
    keyword = 'Bearer'

class PostViewSet(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    authentication_classes = [BearerAuthentication,]
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'data': serializer.data})

    def create(self, request, *args, **kwargs):
        data = {}
        data['user_id'] = request.user.pk
        data['title'] = request.data['title']
        data['content'] = request.data['content']
        if request.data['image']:
            data['image'] = request.data['image']
        else:
            data['image'] = None

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response({'data': serializer.data})
    
    @action(detail=True, methods=['get'])
    def get_comments(self, request, *args, **kwargs):
        post = self.get_object()
        if 'pk' in kwargs:
            comments = Comment.objects.filter(post=post, id=int(kwargs['pk']))
        else:
            comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(instance=comments, many=True)
        return Response({'data': serializer.data})

    @action(detail=True, methods=['post'])
    def post_comment(self, request, *args, **kwargs):
        post = self.get_object()
        comment = {}
        comment['post'] = post.pk
        comment['body'] = request.data['body']
        comment['creator_id'] = request.user.id
        serializer = CommentSerializer(data=comment)

        data = {}
        response_status = status.HTTP_201_CREATED
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data['data'] = serializer.data
        else:
            data['message'] = 'The given data was invalid.'
            data['errors'] = serializer.errors
            response_status = status.HTTP_422_UNPROCESSABLE_ENTITY
        
        return Response(data, status=response_status)
        
        
    
    