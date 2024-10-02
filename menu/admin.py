from django.contrib import admin
from .models import Menu,Menu_iced
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=['drink_name','price_s','price_l']

@admin.register(Menu_iced)
class Menu_icedAdmin(admin.ModelAdmin):
    list_display=['drink_name','price_s','price_l']