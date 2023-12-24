from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body',)
    list_filter = ('is_published',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'version_number', 'version_name', 'version_flag',)
