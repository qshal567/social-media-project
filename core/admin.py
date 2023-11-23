from django.contrib import admin
from .models import Profile, Post, Likepost, FollowersCount


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Likepost)
admin.site.register(FollowersCount)