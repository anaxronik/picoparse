from django.contrib import admin

from .models import Post, Tag


class TagInLine(admin.TabularInline):
    model = Tag
    extra = 1


class PostAdmin(admin.ModelAdmin):
    # Задаем поля которые можно редактировать в админке
    fieldsets = [
        ('Названия', {'fields': ['title', 'origin']}),
        ('Даты', {'fields': ['pub_date']}),
        ('Текст', {'fields': ['text']})
    ]
    # inlines = [TagInLine]

    # поля показываемые в списке всех постов
    list_display = ['title', 'pub_date']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
