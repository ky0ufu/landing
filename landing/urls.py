from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'landing'

urlpatterns = [
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('news/', views.news, name='news'),
    path('', views.index, name='main'),

    path('info/', views.info, name='info'),

    path('press/<slug:slug>/', views.press_detail, name='press_detail'),
    path('press/', views.press, name='press'),

    path('document/', views.document, name='document'),
    path('contact/', views.conatct, name='contact'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # path('announcement/<slug:slug>/', views.announcement_detail, name='announcement_detail'),
    # path('announcement/', views.announcement, name='announcement'),

    # path('photo/<slug:slug>/', views.photo_detail, name='photo_detail'),
    # path('photo/', views.photo, name='photo'),

    # path('video/<slug:slug>/', views.video_detail, name='video_detail'),
    # path('video/', views.video, name='video'),