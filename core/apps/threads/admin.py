from core.apps.threads.models import Comment, Community, Likes, Tag, Thread
from django.contrib import admin

admin.site.register(Tag)
admin.site.register(Community)
admin.site.register(Thread)
admin.site.register(Comment)
admin.site.register(Likes)
