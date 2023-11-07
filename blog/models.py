"""

Основные модели приложения blog.

"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    """Менеджер, который позволит извлекать посты, используя обозначение Post.published.all()."""
    def get_queryset(self):
        """
        Набор запросов QuerySet, фильтрующий посты по их статусу и
        возвращающий поочередный набор запросов QuerySet, содержащий
        посты только со статусом PUBLISHED.
        """
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """
    Это модель данных для постов блога.

    Посты будут иметь заголовок, короткую метку под названием slug и тело поста.
    Метод timezone.now возвращает текущую дату/время в формате, зависящем от часового пояса.
    При применении параметра auto_now_add дата будет сохраняться
    автоматически во время создания объекта;
    При применении параметра auto_now дата будет обновляться автоматически во время
    сохранения объекта.
    Используется related_name, чтобы указывать имя обратной связи, от User к Post.
    """

    class Status(models.TextChoices):
        """В постах будут использоваться статусы Draft (Черновик) и Published (Опубликован)."""
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )
    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        """

        По умолчанию посты будут возвращаться в обратном хронологическом порядке.
        Добавлена опция indexes.

        """
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        """

        Метод возвращает строковый литерал с удобочитаемым представлением объекта.

        """
        return self.title
