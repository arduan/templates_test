
from django.contrib import admin
from django.urls import path

from test_app.views import index
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    # path('', views.blog),
    path('', views.index_blog),

]
