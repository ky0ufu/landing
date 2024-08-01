from django.contrib import admin

from .models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'thumbnail', 'get_tags', 'created_at')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags', 'photos',)

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'thumbnail', 'get_tags', 'created_at')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags', 'photos',)

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'


@admin.register(PhotoReport)
class PhotoReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'thumbnail', 'get_tags', 'created_at')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags', 'photos',)


    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'


@admin.register(Press)
class PressAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'thumbnail', 'get_tags', 'created_at')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags', 'photos',)


    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'thumbnail', 'get_tags', 'video_url', 'video_file', 'created_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('region', 'decan', 'university', 'site_name', 'university_url', 'slug',)
    search_fields = ('decan','university',)
    prepopulated_fields = {'slug': ('decan','university')}


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file',)
    search_fields = ('title',)


@admin.register(RegionSites)
class RegionSitesAdmin(admin.ModelAdmin):
    list_display = ('region', 'site_url', 'site_name')
    search_fields = ('region',)