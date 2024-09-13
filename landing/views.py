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


def index(request):
    objects_count = 4
    news = News.objects.order_by('-created_at')[:objects_count]

    text = EditableText.objects.get(key='hello-text').content

    is_editor = is_editor_or_superuser(request.user)

    head_image = HeadImage.objects.all().first()

    context = {
        'news': news,
        'text': text,
        'is_editor': is_editor,
        'head_image': head_image,
    }
    return render(request, 'core/index.html', context)



def news_detail(request, slug):
    event = get_object_or_404(News, slug=slug)
    context = {'event': event}

    return render(request, 'details/news_detail.html', context)


def document(request):
    documents = Document.objects.all()
    context = {
        'documents': documents,
    }
    return render(request, 'layer_s/documents.html', context)


def conatct(request):

    text = EditableText.objects.get(key='contacts').content
    context = {
        'text': text,
        'is_editor':  is_editor_or_superuser(request.user),
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

    council_text = EditableText.objects.get(key='council-text').content


    context = {
        'leads': leads,
        'councils': councils,
        'presidium': presidium,
        'is_editor':  is_editor_or_superuser(request.user),
        'council_text': council_text,
    }
    return render(request, 'about.html', context)


def region_info(request, slug):
    
    region = get_object_or_404(Region, slug=slug)

    
    context = {
        'region': region
    }

    return render(request, 'layer_s/region_info.html', context)


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test



def is_editor_or_superuser(user):

    if user.is_authenticated:
        return user.is_superuser or user.groups.filter(name='Редактор').exists()
    return False


@csrf_exempt
@require_POST
@user_passes_test(is_editor_or_superuser)
def update_text(request):
    key = request.POST.get('key')
    content = request.POST.get('content')


    try:
        text_object = EditableText.objects.get(key=key)
        text_object.content = content
        text_object.save()

        return JsonResponse({'success': True})
    except EditableText.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Text not found'}, status=404)
    

@csrf_exempt
@require_POST
@user_passes_test(is_editor_or_superuser)
def update_council_text(request):
    council_id = request.POST.get('council_id')
    council_name = request.POST.get('council_name')
    chairperson_name = request.POST.get('chairperson_name')
    chairperson_description = request.POST.get('chairperson_description')

    try:
        Council.objects.filter(id=council_id).update(name=council_name)


        full_name = chairperson_name.split(' ')
        last_name = full_name[0] if len(full_name) > 0 else ''
        name = full_name[1] if len(full_name) > 1 else ''
        surname = full_name[2] if len(full_name) > 2 else ''

        chairperson = Council.objects.get(id=council_id).chairperson
 
        chairperson.last_name = last_name
        chairperson.name = name
        chairperson.surname = surname
        chairperson.save()

        Council.objects.filter(id=council_id).update(chairperson_describtion=chairperson_description)

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})



@csrf_exempt
@require_POST
@user_passes_test(is_editor_or_superuser)
def update_presidium(request):

    id = request.POST.get('id')
    member_name = request.POST.get('name')
    description = request.POST.get('description')

    try:
        member = PresidumMember.objects.get(id=id).member

        full_name = member_name.split(' ')
        last_name = full_name[0] if len(full_name) > 0 else ''
        name = full_name[1] if len(full_name) > 1 else ''
        surname = full_name[2] if len(full_name) > 2 else ''

        member.last_name = last_name
        member.name = name
        member.surname = surname
        member.describtion = description
        member.save()

        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


