from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

# Register your models here.

admin.site.register(ProImag)

admin.site.register(ProductReview)

admin.site.register(Home_images)


class ProductImageInline(admin.TabularInline):
    model = ProImag
    extra = 6


class ProductAdmin(TranslationAdmin):

    list_display = ['Book_name', 'category', 'slug',  'price',  'created',
                    'updated']
    list_filter = [ 'created', 'updated']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('Book_name',)}
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)


# class CategoryAdmin(admin.ModelAdmin):
# 	list_display = ('category_name', 'slug',)
# 	prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Category)

