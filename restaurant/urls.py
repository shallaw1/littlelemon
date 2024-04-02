from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register("tables", views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name="menu-list"),
    path('menu/<int:pk>/', views.SingleItemView.as_view(), name="menu-detail"),
    path('api-token-auth/', obtain_auth_token),
] + router.urls
