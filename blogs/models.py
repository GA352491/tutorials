from django.db import models
from tinymce import HTMLField


# Create your models here.

class Course(models.Model):
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.course


class Category(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class TutorialBlog(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = HTMLField('Content')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Images(models.Model):
    img = models.ImageField(upload_to='blogs/static/media')


