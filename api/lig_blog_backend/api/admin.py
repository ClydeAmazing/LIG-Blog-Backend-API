from django.contrib import admin
from api.models import Post, Comment

# class PostsAdmin(admin.ModelAdmin):


# class CommentsAdmin(admin.ModelAdmin):

admin.site.register(Post)
admin.site.register(Comment)