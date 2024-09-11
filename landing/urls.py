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

    path('document/', views.document, name='document'),
    path('contact/', views.conatct, name='contact'),

    path('region_info/<slug:slug>', views.region_info, name='region'),

    path('update-text/', views.update_text, name='update_text'),
    path('update-council', views.update_council_text, name='update_council'),
    path('update-presidium', views.update_presidium, name='update_presidium'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)