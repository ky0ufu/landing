from django.db import models
from pytils.translit import slugify
from datetime import datetime
from django.urls import reverse
from django.utils import timezone
from PIL import Image
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
import os
import shutil
from django.core.files import File


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Название тэга')

    def __str__(self):
        return self.name
    

class BaseModel(models.Model):

    title = models.CharField(max_length=200, verbose_name='Заголовок')

    slug = models.SlugField(max_length=250, unique=True, verbose_name='Слаг(юрл)')

    image = models.ImageField(upload_to='images/', default='placeholder.jpg', verbose_name='Изображение')

    thumbnail = models.ImageField(upload_to='thumbnails/', verbose_name='Миниатюра', blank=True, null=True)

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
        super().save(*args, **kwargs)
        

        thumb_path = self.thumbnail.path


        max_thumb = (1100, 675)


        self.resize_img(thumb_path, max_thumb)
    
    def create_thumbnail(self):
        """
        Создаем копию изображения и изменяем размер для миниатюры.
        """
        img_path = self.image.path
        thumb_path = os.path.join(os.path.dirname(self.image.path), 'thumbnails', os.path.basename(self.image.path))

        # Копируем изображение в папку миниатюр
        if not os.path.exists(os.path.dirname(thumb_path)):
            os.makedirs(os.path.dirname(thumb_path))

        shutil.copy(img_path, thumb_path)


        self.resize_img(thumb_path, (1100, 675))

        # Сохраняем путь к миниатюре в поле thumbnail
        self.thumbnail.save(os.path.basename(thumb_path), File(open(thumb_path, 'rb')), save=False)


    def resize_img(self, path, size):
        with Image.open(path) as img:
            img = img.resize(size, Image.LANCZOS)
            img.save(path)


class Photo(models.Model):
    image = models.ImageField(blank=True, upload_to='photos/', verbose_name='Изображение')


    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        string = self.image.url.split('/')[-1].split('.')[0]
        return f'{string}'
    
    def get_absolute_url(self):
        return reverse("photo_detail", kwargs={"id": self.id})
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    


class News(BaseModel):

    text = models.TextField(verbose_name='Текст новости')
    photos = models.ManyToManyField('Photo', related_name='news_photos', blank=True, verbose_name='Изображения')

    def get_absolute_url(self):
        return reverse("news", kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'




class Member(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    surname = models.CharField(max_length=255, verbose_name='Отчество')

    describtion = models.TextField(verbose_name='Иноформация', blank=True, null=True)

    profile_image = models.ImageField(upload_to='images/', default='placeholder.jpg', verbose_name='Изображение')
    
    url = models.URLField(null=True, blank=True, verbose_name='Ссылка на сайт')
    

    class Meta:
        verbose_name = 'Член совета'
        verbose_name_plural = 'Члены совета'



    def __str__(self):
        return f'{self.last_name} {self.name} {self.surname}'

    

    def get_absolute_url(self):
        return reverse("member", kwargs={"slug": self.__str__()})
    

    def photo_tag(self):
        if self.profile_image:
            return mark_safe(f'<img src="{self.profile_image.url}" width="150" height="150" />')
        return "No Image"

    photo_tag.short_description = 'Photo'
    photo_tag.allow_tags = True


class Document(models.Model):
    title=models.CharField(max_length=255, verbose_name='Название документа')
    file=models.FileField(upload_to='documents/', verbose_name='Файл документа')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    

    
class Council(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название совета')

    chairperson = models.OneToOneField(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='council_chair', verbose_name='Председатель')

    chairperson_describtion = models.TextField(verbose_name='Описание председателя')

    url = models.URLField(null=True, blank=True, verbose_name='Ссылка на сайт')
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Региональный совет ректоров'
        verbose_name_plural = 'Региональные советы ректоров'


class PresidumMember(models.Model):
    member = models.OneToOneField(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='member', verbose_name='Член президиума')


    class Meta:
        verbose_name = 'Член президиума'
        verbose_name_plural = 'Участники президиума'

    
    def __str__(self) -> str:
        return self.member.__str__()


