from django.urls import path
from . import views

app_name = 'sam_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('modules', views.modules, name='modules'),
    path('modules/create', views.module_create, name='module_create'),
    path('modules/change_status/<str:module_name>', views.change_status, name='change_status'),
    # path('admin', admin.site.urls, name='admin_view'),
]