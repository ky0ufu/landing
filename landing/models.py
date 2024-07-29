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

    title = models.CharField(max_length=200)

    slug = models.SlugField(max_length=250, unique=True)

    image = models.ImageField(upload_to='images/', default='placeholder.jpg')

    thumbnail = models.ImageField(upload_to='thumbnails/', default='placeholder/default_image.jpg')

    tags = models.ManyToManyField('Tag', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) 

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
    image = models.ImageField(blank=True, upload_to='photos/')
    title = models.TextField()

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse("photo_detail", kwargs={"id": self.id})
    
    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.image.url.split('/')[-1].split('.')[0]
        return super().save(*args, **kwargs)
    


class News(BaseModel):

    text = models.TextField()
    photos = models.ManyToManyField('Photo', related_name='news_photos', blank=True)

    def get_absolute_url(self):
        return reverse("news", kwargs={'slug': self.slug})


class Press(BaseModel):

    text = models.TextField()
    photos = models.ManyToManyField('Photo', related_name='press_photos', blank=True)

    def get_absolute_url(self):
        return reverse("press", kwargs={'slug': self.slug})


class PhotoReport(BaseModel):

    text = models.TextField()
    photos = models.ManyToManyField('Photo', related_name='report_photos', blank=True)

    def get_absolute_url(self):
        return reverse("report", kwargs={'slug': self.slug})
    

class Announcement(BaseModel):

    text = models.TextField()
    photos = models.ManyToManyField('Photo', related_name='ann_photos', blank=True)

    def get_absolute_url(self):
        return reverse("announcement", kwargs={"slug": self.slug})


class Video(BaseModel):

    video_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)

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