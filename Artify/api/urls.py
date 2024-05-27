from django.urls import path, include

urlpatterns = [
    path('users/', include('user.urls')),
    path('posts/', include('post.urls')),
    path('events/', include('event.urls'))
]