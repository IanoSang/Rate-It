from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/', views.profile, name='profile'),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('search/', views.search_project, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
