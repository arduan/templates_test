
from django.contrib import admin
from django.urls import path

from test_app.views import index
from blog import views

urlpatterns = [
     path('', index),
    # path('', views.index_blog),
    # path('', views.blog),
    path('admin/', admin.site.urls),




]
