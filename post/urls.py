from django.urls import path
from .views import PostView, DeletePostView, FindPostView

urlpatterns = [
    path('list', PostView.as_view()),
    path('create', PostView.as_view()),
    path('<int:pk>/delete', DeletePostView.as_view()),
    path('<int:pk>/get/', FindPostView.as_view())
]