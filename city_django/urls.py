from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_swagger.views import get_swagger_view

from common.routers import DefaultRouter
from rbac.api.urls import router as rbac_router

router = DefaultRouter()
router.extend(rbac_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', get_swagger_view(title='API')),
    path('api/', include(router.urls))
]
