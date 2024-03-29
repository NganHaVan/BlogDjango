import datetime
from time import gmtime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


def image_directory_path(instance, filename):
    return 'images/user_{}/({})-{}'.format(instance.user.id, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, upload_to=image_directory_path,
                                    default="personal-user-illustration-@2x.png")

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def filter_approve_comment(self):
        return self.comments.filter(approve_comment=True)

    # Redirect after creating a post
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("blog:post_list")

    def __str__(self):
        return self.content
