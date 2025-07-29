from django.urls import path

from . import views

urlpatterns = [
    path('hello_world', views.hello_world),
    path('start_simulation', views.start_simulation),
    path('step_simulation', views.step_simulation),
    path('get_state', views.get_state),
    path('reset_simulation', views.reset_simulation),
    path('create_grid', views.create_grid),
]