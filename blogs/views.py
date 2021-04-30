from django.shortcuts import render
from .models import Course, Category, TutorialBlog

from django.template.loader import render_to_string
from django.http import JsonResponse

import random


# Create your views here.

def home(request):
    courses = Course.objects.all()
    a = [
        ' background: radial-gradient(53.85% 64.23% at 79.27% 51.46%, #100101 28.38%, rgba(34, 3, 3, 0) 100%), #440606;',
        'background:radial-gradient(53.85% 64.23% at 79.27% 51.46%, #100101 28.38%, rgba(34, 3, 3, 0) 100%), #440606;',

        'background-image: linear-gradient(160deg,  #590202 0%,#0D0D0D 0%,#010440  );',
        'background: radial-gradient(81.91% 68.48% at 12.19% 74.98%, #808080 0%, #808080 0%, rgba(255, 255, 255, 0) 81.37%), #000000;',
    ]
    b = random.choice(a)

    context = {'courses': courses, 'b': b}
    return render(request, 'home/home.html', context)


def tutorial(request, pk):
    course = Course.objects.get(id=pk)
    # print(course.id)
    category = Category.objects.filter(course=course)
    t = TutorialBlog.objects.filter(course=course.id).first()
    print(t)
    t2 = TutorialBlog.objects.filter(course=course.id).first()
    # print(t2)
    blogs = TutorialBlog.objects.filter(course=course)
    # print(blogs)

    context = {'category': category, 't': t, 'blogs': blogs, 'course': course, }
    return render(request, 't-view.html', context)


def tutorial_view(request, pk):
    blog = TutorialBlog.objects.get(id=pk)
    course = blog.course
    category = Category.objects.filter(course=course)
    blogs = TutorialBlog.objects.filter(course=course)

    context = {'blog': blog, 'category': category, 'blogs': blogs, 'course': course, }

    return render(request, 'tutorial/tutorial_view.html', context)



def tut(request):
    if request.is_ajax():
        pk = request.GET.get('a')
        blog = TutorialBlog.objects.get(id=pk)
        course = blog.course
        # print(blog)

        category = Category.objects.filter(course=course)
        blogs = TutorialBlog.objects.filter(course=course)
        context = {'blog': blog, 'category': category, 'blogs': blogs, 'course': course, }
        blo = render_to_string('tutorial/tutorial_view2.html', context, request=request)

        data = {'blo': blo}
        return JsonResponse(data)
