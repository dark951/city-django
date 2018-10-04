from django.contrib import admin
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', get_swagger_view(title='API'))
]
