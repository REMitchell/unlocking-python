from django.contrib import admin
from posts import models


class PostAdmin(admin.ModelAdmin):
    # Changes what's displayed on the Admin site
    list_display = ('title',)


admin.site.register(models.Post, PostAdmin)
