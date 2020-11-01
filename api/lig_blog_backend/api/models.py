from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils.text import slugify
import os

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_flag = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    image = models.URLField(blank=True, null=True)
    # image = models.ImageField(upload_to='images', null=True, blank=True)

    def save(self, *args, **kwargs):
        slug_text = slugify('{}-{}'.format(str(self.pk), self.title))
        self.slug = slug_text[:50]
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    commentable_type = models.CharField(max_length=50, null=True, blank=True) # App \\ Post ??
    commentable_id = models.BooleanField(default=True)
    creator_id = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Comment: {}'.format(self.title)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=Post)
def generate_slug(sender, instance, created, **kwargs):
    if created:
        slug_text = slugify('{}-{}'.format(str(instance.pk), instance.title))
        instance.slug = slug_text[:50]
        instance.save()