from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.text import slugify

class User(models.Model):
    pass


class Publication(models.Model):
    title = models.CharField(max_length=300)
    url = models.URLField(blank=True, null=True)
    abstract = models.TextField()
    description = models.TextField()
    likes =models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300,unique=True, blank=True, default="", editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    user_id = models.ForeignKey(User, related_name="commented_user", on_delete=models.CASCADE)
    publication_id = models.ForeignKey(Publication,related_name="publications_commented", on_delete=models.CASCADE)
    comment_value = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Likes(models.Model):
    user_id = models.ForeignKey(User, related_name="liked_user", on_delete=models.CASCADE)
    publication_id=models.ForeignKey(Publication, related_name="publications_liked",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Saved(models.Model):
    user_id = models.ForeignKey(User, related_name="saved_user", on_delete=models.CASCADE)
    publication_id=models.ForeignKey(Publication, related_name="publications_saved", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

