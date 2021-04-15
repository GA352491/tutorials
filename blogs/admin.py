from django.contrib import admin
from .models import Course, Category, TutorialBlog,Images

# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(TutorialBlog)
admin.site.register(Images)
