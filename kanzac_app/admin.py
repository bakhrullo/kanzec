from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin.options import TabularInline
from django.utils.safestring import mark_safe

from import_export.admin import ImportExportMixin

from .models import *
from .resources import OtherResource


class VideoAdminInline(TabularInline):
    extra = 1
    model = Video


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tg_id', 'phone', 'created_date']
    list_filter = ['name', 'tg_id', 'phone', 'created_date']
    search_fields = ['name',  'tg_id', 'phone']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date']
    list_filter = ['name', 'created_date']
    list_editable = ['name']
    search_fields = ['name']
    fields = ['name', 'created_date']
    readonly_fields = ['created_date']


class ProductAdmin(admin.ModelAdmin):
    inlines = (VideoAdminInline,)
    list_display = ['id', 'get_image', 'price', 'category', 'quan', 'created_date']
    list_editable = ['price', 'category', 'quan']
    search_fields = ['price']

    def get_image(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_image.short_description = 'Rasim'


class OrderAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_classes = [OtherResource]
    list_display = ['id', 'user', 'product', 'created_date']
    list_filter = ['user', 'product', 'created_date']


admin.site.unregister(Group)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.site_title = 'Admin panel'
admin.site.site_header = 'Admin panel'
