from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from django.forms import ModelForm


class GalleryInline(admin.TabularInline):
    model = Photo

@admin.register(Products)
class OllCheck(admin.ModelAdmin):
    list_display = ['title', 'img_show', 'slug', 'amount']
    list_filter = ['category', 'title']
    inlines = [GalleryInline]

    def img_show(self, obj):
        if obj.img:
            return mark_safe('<img src="{}" alt="" height="50px">'.format(obj.img.url))
        return "None"


admin.site.register(Category)
admin.site.register(Order)

@admin.register(Seo)
class OllCheck(admin.ModelAdmin):
    list_display = ['url']





