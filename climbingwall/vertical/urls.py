from django.urls import path

from . import views

urlpatterns = [
    path('', views.DisplayPageView.as_view(), name='index'),
    path('display', views.DisplayPageView.as_view(), name='display'),
    path('display/<int:boulder_id>', views.request_method, name='led'),
    path('disable',views.turn_off_led_view, name='disable'),
    path('create',views.CreatePageView.as_view(),name='create'),
    path('emp',views.boulder_post_method,name='emp'),
    path('edit/<int:boulder_id>', views.edit_method, name='led'),
    path('delete/<int:boulder_id>', views.delete_method, name='led'),
    path('emp/delete',views.boulder_edit_post_method,name='empDelete')
]
