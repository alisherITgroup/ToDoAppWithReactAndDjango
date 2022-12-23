from django.urls import path
from .views import TodoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"api/v1/todos", TodoViewSet, 'todos')

urlpatterns = router.urls
