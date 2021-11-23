
from django.contrib import admin
from django.urls import path

from test_app.views import index
from blog.views import index_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    path('', index_blog)
]
