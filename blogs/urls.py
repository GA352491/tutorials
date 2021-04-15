from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutorial/<pk>', views.tutorial, name='tutorial'),
    path('tutorial_view/<pk>', views.tutorial_view, name='tutorial_view'),
    path('test/', views.test, name='test'),

]
