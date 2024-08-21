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



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'surname', 'profile_image', 'url',)
    search_fields = ('last_name',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file',)
    search_fields = ('title',)

@admin.register(Council)
class CouncilAdmin(admin.ModelAdmin):
    list_display = ('name', 'chairperson', 'url', )
    search_fields = ('name',)

class MemberInline(admin.TabularInline):
    model = Member
    extra = 1



@admin.register(PresidumMember)
class PresidumMemberAdmin(admin.ModelAdmin):
    exclude = ('limit', )
    list_display = ('member', )