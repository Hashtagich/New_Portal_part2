from django.urls import path

from .views import PostsList, PostDetail, PostsList2

urlpatterns = [
    path('', PostsList.as_view()),
    path('v2/', PostsList2.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('v2/<int:pk>', PostDetail.as_view()),
]
