from django.contrib import admin
from django.urls import path,include
from api.views import apiview
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'',apiview)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include(router.urls))
]