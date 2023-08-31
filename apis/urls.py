from django.urls import path
from . import views

urlpatterns = [
    path('contents/', views.ContentList.as_view()),
    path('content/<int:pk>', views.ContentDetail.as_view()),
    path('search/',views.ContentSearchAPIView.as_view())
]
