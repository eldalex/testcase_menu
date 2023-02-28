from django.contrib import admin
from .models import Menu

class Child(admin.StackedInline):
    model = Menu
    fields = ('name', 'parent', 'url')
    extra = 0


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url')
    inlines = [Child,]

admin.site.register(Menu, MenuAdmin)