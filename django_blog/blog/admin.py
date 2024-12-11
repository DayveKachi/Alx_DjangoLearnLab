from django.contrib import admin
from .models import Post, Profile, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    list_filter = ("author", "published_date")
    search_fields = ("title", "author")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "profile_picture")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "content")
    list_filter = ("author", "post")
    search_fields = ("author", "content")


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, CommentAdmin)
