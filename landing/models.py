from django.db import models
from pytils.translit import slugify
from datetime import datetime
from django.urls import reverse
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    

class BaseModel(models.Model):

    title = models.CharField(max_length=200, verbose_name='Заголовок')

    slug = models.SlugField(max_length=250, unique=True, verbose_name='Слаг(юрл)')

    image = models.ImageField(upload_to='images/', default='placeholder.jpg', verbose_name='Изображение')

    thumbnail = models.ImageField(upload_to='thumbnails/', default='placeholder/default_image.jpg', verbose_name='Миниатюра')

    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Тэги')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания') 

    class Meta:
        abstract = True


    def unique_slug(self):
        unique_slug = slugify(self.title)

        current_datetime = datetime.now()
        current_datetime = current_datetime.strftime("%d_%m_%Y")

        return f"{current_datetime}_{unique_slug}"

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.unique_slug()
        return super().save(*args, **kwargs)
    


class Photo(models.Model):
    image = models.ImageField(blank=True, upload_to='photos/', verbose_name='Изображение')
    title = models.TextField(verbose_name='Заголовок')


    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse("photo_detail", kwargs={"id": self.id})
    
    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.image.url.split('/')[-1].split('.')[0]
        return super().save(*args, **kwargs)
    


class News(BaseModel):

    text = models.TextField(verbose_name='Текст новости')
    photos = models.ManyToManyField('Photo', related_name='news_photos', blank=True, verbose_name='Изображения')

    def get_absolute_url(self):
        return reverse("news", kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Press(BaseModel):

    text = models.TextField(verbose_name='Текст пресс-релиза')
    photos = models.ManyToManyField('Photo', related_name='press_photos', blank=True, verbose_name='Изображения')

    def get_absolute_url(self):
        return reverse("press", kwargs={'slug': self.slug})
    

    class Meta:
        verbose_name = 'Пресс-релиз'
        verbose_name_plural = 'Пресс-релизы'


class PhotoReport(BaseModel):

    text = models.TextField(verbose_name='Текст фоторепортажа')
    photos = models.ManyToManyField('Photo', related_name='report_photos', blank=True, verbose_name='Изображения')

    def get_absolute_url(self):
        return reverse("report", kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Фоторепортаж'
        verbose_name_plural = 'Фоторепортажи'
    

class Announcement(BaseModel):

    text = models.TextField(verbose_name='Текст анонса')
    photos = models.ManyToManyField('Photo', related_name='ann_photos', blank=True, verbose_name='Изображения')

    def get_absolute_url(self):
        return reverse("announcement", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name = 'Анонс'
        verbose_name_plural = 'Анонсы'


class Video(BaseModel):

    video_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')
    video_file = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name='видео файл')


    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def get_absolute_url(self):
        return reverse("video", kwargs={"slug": self.slug})
    

    def get_embeded_url(self):
        if self.video_url:
            # Извлечение идентификатора видео из URL
            video_id = self.video_url.split('v=')[-1]
            if '&' in video_id:
                video_id = video_id.split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        return None
    

class Member(models.Model):
    region = models.CharField(max_length=100, verbose_name='Регион')

    slug = models.SlugField(max_length=250, unique=True, verbose_name='Слаг(юрл)')

    university = models.CharField(max_length=100, verbose_name='Университет')

    decan = models.CharField(max_length=100, verbose_name='Ректор')

    university_url = models.URLField(null=True, blank=True, verbose_name='Ссылка на вуз')

    is_head = models.BooleanField(default=False, verbose_name='Является главной?')

    is_member = models.BooleanField(default=False, verbose_name='Является членом совета ректоров вузов? ')

    is_member_region = models.BooleanField(default=False, verbose_name='Является членом регионального совета ректоров вузов? ')


    class Meta:
        verbose_name = 'Член совета'
        verbose_name_plural = 'Члены совета'

    def unique_slug(self):
        slug_decan = slugify(self.decan)
        slug_university = slugify(self.university)

        return f"{self.id}_{slug_university}_{slug_decan}"

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.unique_slug()
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("member", kwargs={"slug": self.slug})
    

class Document(models.Model):
    title=models.CharField(max_length=255, verbose_name='Название документа')
    file=models.FileField(upload_to='documents/', verbose_name='Файл документа')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    

