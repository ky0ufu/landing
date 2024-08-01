from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator

def get_context(obj, page_number):

    paginator = Paginator(obj, 10)
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}

    return context

def news(request):
    news_list = News.objects.order_by('-created_at')

    page_number = request.GET.get('page')
    
    context = get_context(news_list, page_number)

    return render(request, 'layer_s/news.html', context)

def press(request):
    press = Press.objects.order_by('-created_at')

    page_number = request.GET.get('page')
    
    context = get_context(press, page_number)
    
    return render(request, 'layer_s/press.html', context)

def announcement(request):
    announcements = Announcement.objects.order_by('-created_at')

    page_number = request.GET.get('page')
    
    context = get_context(announcements, page_number)
    
    return render(request, 'layer_s/announcements.html', context)


def photo(request):
    photos = PhotoReport.objects.order_by('-created_at')

    page_number = request.GET.get('page')
    
    context = get_context(photos, page_number)
    
    return render(request, 'layer_s/photo.html', context)


def video(request):
    videos = Video.objects.order_by('-created_at')

    page_number = request.GET.get('page')
    
    context = get_context(videos, page_number)
    
    return render(request, 'layer_s/video.html', context)



def index(request):
    objects_count = 4
    media_count = 2
    news = News.objects.order_by('-created_at')[:objects_count]

    presses = Press.objects.order_by('-created_at')[:objects_count]

    announcements = Announcement.objects.order_by('-created_at')[:objects_count]

    reports = PhotoReport.objects.order_by('-created_at')[:media_count]

    documents = Document.objects.all()

    videos = Video.objects.order_by('-created_at')[:media_count]
    context = {
        'news': news,
        'presses': presses,
        'announcements': announcements,
        'reports': reports,
        'videos': videos,
        'documents': documents,
    }
    return render(request, 'core/index.html', context)



def news_detail(request, slug):
    event = get_object_or_404(News, slug=slug)
    context = {'event': event}

    return render(request, 'details/news_detail.html', context)


def press_detail(request, slug):
    press = get_object_or_404(Press, slug=slug)
    context = {'press': press}

    return render(request, 'details/press_detail.html', context)


def announcement_detail(request, slug):
    announcement = get_object_or_404(Announcement, slug=slug)
    context = {'announcement': announcement}

    return render(request, 'details/announcement_detail.html', context)

def photo_detail(request, slug):
    report = get_object_or_404(PhotoReport, slug=slug)
    context = {'report': report}

    return render(request, 'details/photo_detail.html', context)


def video_detail(request, slug):
    video = get_object_or_404(Video, slug=slug)
    context = {'video': video}

    return render(request, 'details/video_detail.html', context)


def info(request):

    members = Member.objects.filter(is_member=True)
    members_region = RegionSites.objects.all()


    context = {
        'members': members,
        'members_region': members_region
    }
    return render(request, 'about.html', context)