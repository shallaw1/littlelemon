from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("user", views.UserViewSet)

urlpatterns = router.urls
