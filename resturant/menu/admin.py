from django.contrib import admin

# Register your models here.
from menu.models import Dish


class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_editable = ['price']


admin.site.register(Dish, DishAdmin)
