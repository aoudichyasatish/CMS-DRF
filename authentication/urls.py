from django.urls import path, include, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from .views import UserLogIn, UserViewSet, RegisterAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/v1/',include(router.urls)),
    path('login/', UserLogIn.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
]