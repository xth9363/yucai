from django.contrib import admin

# Register your models here.
from main import models


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20  # 让每页显示几条记录的设置
    list_display = ('name', 'active', 'hot')


class NewsAdmin(admin.ModelAdmin):
    list_per_page = 20  # 让每页显示几条记录的设置
    list_display = ('title', 'content')


class OtherTextAdmin(admin.ModelAdmin):
    list_per_page = 20  # 让每页显示几条记录的设置
    list_display = ('name', 'content','code')
    # readonly_fields = ('code',)


class OtherRichTextFieldAdmin(admin.ModelAdmin):
    list_per_page = 20  # 让每页显示几条记录的设置
    list_display = ('name', 'content','code')
    # readonly_fields = ('code',)


class OtherImagesAdmin(admin.ModelAdmin):
    list_per_page = 20  # 让每页显示几条记录的设置
    list_display = ('name', 'content','code')
    # readonly_fields = ('code',)


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.News, NewsAdmin)

admin.site.register(models.OtherText, OtherTextAdmin)
admin.site.register(models.OtherRichText, OtherRichTextFieldAdmin)
admin.site.register(models.OtherImages, OtherImagesAdmin)
