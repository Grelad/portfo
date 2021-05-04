from django.contrib import admin

from portfo.apps.portfolio.models import Comment, Image, Portfolio

admin.site.register(Portfolio)
admin.site.register(Image)
admin.site.register(Comment)
