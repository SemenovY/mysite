"""Панель администратора."""
from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Отображаемые на странице списка постов поля
    list_display = ["title", "slug", "author", "publish", "status"]
    # Боковая панель, которая позволяет фильтровать результаты
    list_filter = ["status", "created", "publish", "author"]
    # Строка поиска
    search_fields = ["title", "body"]
    # При вводе заголовка нового поста поле slug заполняется автоматически
    # данными, вводимыми в поле title
    prepopulated_fields = {"slug": ("title",)}
    # Виджет для отбора ассоциированных объектов для поля author модели Post
    raw_id_fields = ["author"]
    # Навигационные ссылки для навигации по иерархии дат
    date_hierarchy = "publish"
    # По умолчанию посты упорядочены по столбцам STATUS (Статус) и
    # PUBLISH (Опубликован)
    ordering = ["status", "publish"]
