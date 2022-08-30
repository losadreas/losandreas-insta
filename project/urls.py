from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from user.views import PostView, CreatePost, likeview, HomeView, login_error_view
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('users/', include('user.urls')),
    path('post/', PostView.as_view(), name='post'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('like/<int:pk>/', likeview, name='like_post'),
    path('login_error/', login_error_view, name='login_error'),
    path('', include('social_django.urls', namespace='social'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'user.views.login_error_view'

