from django.contrib import admin
from .models import Shop
# Register your models here.


class ShopAdmin(admin.ModelAdmin):
    list_display = ('url','description')

admin.site.register(Shop, ShopAdmin)

