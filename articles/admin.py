from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline):  # or admin.StackedInline

    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]


admin.site.register(Article)
admin.site.register(Comment)
