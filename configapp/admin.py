from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


class ShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['id', 'title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'publish_date', 'orders', 'active']
    list_filter = ['active', 'price', 'publish_date']
    search_fields = ['id', 'title']
    readonly_fields = ['main_image']
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'publish_date', 'price', 'image', 'main_image', 'orders', 'active')
        }),
        ('Shops and Categories', {
            'fields': ('shop', 'categories')
        })
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(orders_count=models.Count('orders'))

    def order_count(self, obj):
        return obj.orders_count

    order_count.admin_order_field = 'orders_count'
    actions = ['make_inactive', 'make_active']

    def make_inactive(self, request, queryset):
        queryset.update(active=False)

    def make_active(self, request, queryset):
        queryset.update(active=True)

    make_inactive.short_description = "Mark selected products as inactive"
    make_active.short_description = "Mark selected products as active"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Role)
admin.site.register(CustomUser, UserAdmin)

