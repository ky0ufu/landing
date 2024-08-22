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

# def announcement(request):
#     announcements = Announcement.objects.order_by('-created_at')

#     page_number = request.GET.get('page')
    
#     context = get_context(announcements, page_number)
    
#     return render(request, 'layer_s/announcements.html', context)


# def photo(request):
#     photos = PhotoReport.objects.order_by('-created_at')

#     page_number = request.GET.get('page')
    
#     context = get_context(photos, page_number)
    
#     return render(request, 'layer_s/photo.html', context)


# def video(request):
#     videos = Video.objects.order_by('-created_at')

#     page_number = request.GET.get('page')
    
#     context = get_context(videos, page_number)
    
#     return render(request, 'layer_s/video.html', context)



def index(request):
    objects_count = 4
    news = News.objects.order_by('-created_at')[:objects_count]
    text = "Совет ректоров высших учебных заведений Дальневосточного федерального округа является составной частью государственно-общественной системы управления высшим образованием в Российской Федерации и создан в целях содействия развитию и координации связей вузов региона по эффективному использованию интеллектуального потенциала вузов в интересах развития производительных сил, определения экономических и социально-гуманитарных мер по улучшению демографической ситуации в Дальневосточном федеральном округе; разработки и реализации прогнозов и программ развития округа, ориентированных на решение проблем региона средствами науки и образования; содействия в деятельности полномочного представителя Президента Российской Федерации в Дальневосточном федеральном округе"
    print(News.objects.order_by('-created_at').first().thumbnail)
    context = {
        'news': news,
        'text': text,
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


def document(request):
    documents = Document.objects.all()
    context = {
        'documents': documents,
    }
    return render(request, 'layer_s/documents.html', context)


def conatct(request):
    adress = "690922, Приморский край, г. Владивосток, о. Русский, п. Аякс, 10"
    email = "rectorsdfo@dvfu.ru"

    secretary = "Гридасов Александр Валентинович"
    secretary_phone = "8 (423) 265 24 24 (доб.2123)"
    secretary_email = "gridasov.av@dvfu.ru"

    lead_specialist = "Фомен Дарья Андреевна"
    lead_phone = "8 (423) 265 24 24 (доб. 2332)"
    lead_email = "fomen.dan@dvfu.ru"

    techlead = "Юсипов Евгений Ансарович"
    techlead_phone = "8 (423) 265 24 24 (доб. 2716)"
    techlead_email = "yusipov.ea@dvfu.ru"

    context = {
        'secretary': secretary,
        'secretary_phone': secretary_phone,
        'secretary_email': secretary_email,
        'lead_specialist': lead_specialist,
        'lead_phone': lead_phone,
        'lead_email': lead_email,
        'techlead': techlead,
        'techlead_phone': techlead_phone,
        'techlead_email': techlead_email,
    }

    return render(request, 'layer_s/contacts.html', context)



def info(request):
    head = Member.objects.filter(describtion__icontains='председатель Совета ректоров вузов Дальневосточного федерального округа').first()
    
    subheads = Member.objects.filter(describtion__icontains='заместитель председателя Совета ректоров вузов Дальневосточного федерального округа').all()
    leads = []
    leads.append(head)
    for subhead in subheads:
        leads.append(subhead)

    councils = Council.objects.all()
    presidium = PresidumMember.objects.all()

    context = {
        'leads': leads,
        'councils': councils,
        'presidium': presidium,
    }
    return render(request, 'about.html', context)