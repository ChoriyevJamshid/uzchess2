from django.contrib import admin

from course import models


class CommentInline(admin.TabularInline):
    model = models.Comment
    extra = 0


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Course)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (CommentInline,)
    pass


@admin.register(models.Chapter)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Lesson)
class CategoryAdmin(admin.ModelAdmin):
    pass






