from django.contrib import admin
from .models import Service, ServiceOffer, SubService, Review, Page

# Register your models here.

class ServiceOfferInline(admin.TabularInline):
    model = ServiceOffer
    extra = 0

@admin.register(SubService)
class SubServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['service',]


class SubServiceInline(admin.StackedInline):
    model = SubService
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name' ,'description', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ServiceOfferInline, SubServiceInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'link_on_footer']
    list_editable = ['link_on_footer']
    prepopulated_fields = {'slug': ('title',)}