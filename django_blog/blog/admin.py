from django.contrib import admin
from .models import Post, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    list_filter = ("author", "published_date")
    search_fields = ("title", "author")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "profile_picture")


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
