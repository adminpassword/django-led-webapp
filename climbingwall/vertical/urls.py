from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('display', views.DisplayPageView.as_view(), name='display'),
    path('display/<int:boulder_id>', views.request_method, name='led'),
]
