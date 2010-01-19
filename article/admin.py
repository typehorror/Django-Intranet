from django.contrib import admin
from django import forms
from django.db import models
from models import Article, Comment, FeaturedArticle
from attachments.admin import AttachmentInlines
from django.conf import settings

class CommentAdmin(admin.ModelAdmin):
    """
    Comment admin page
    """
    search_fields = ('email_address', 'body')
    list_filter = ('status', 'creation_date')
    list_display = ('email_address', 'website', 'creation_date', 'status')

class CommentInline(admin.TabularInline):
    """
    Display the comment linked to the article on
    the article admin page.
    """
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    """
    Article admin page
    """
    search_fields = ('title','tags')
    list_filter = ('is_visible','modification_date')
    list_display = ('title','creation_date','modification_date','author')

    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('%sjs/ckeditor/ckeditor.js' % settings.STATIC_URL,) # The , at the end of this list IS important.
    inlines = [CommentInline,AttachmentInlines]

class FeaturedArticleAdmin(admin.ModelAdmin):
    """
    Featured Article admin page
    """
    list_filter = ('is_visible','modification_date')
    list_display = ('id', 'creation_date', 'is_visible')

admin.site.register(FeaturedArticle, FeaturedArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
