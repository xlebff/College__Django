from django.contrib import admin
from .models import Category, Feature, Zone

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'popular', 'tag')
    list_filter = ('category', 'popular')
    search_fields = ('title', 'description')
    list_editable = ('price', 'popular')
    ordering = ('title',)
    filter_horizontal = ('features',)