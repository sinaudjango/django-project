from django.contrib import admin
from .models import Post


# Register your models here.
class postAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'publish', 'update', ]

admin.site.register(Post, postAdmin)