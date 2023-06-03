from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель групп"""

    title = models.CharField('Название сообщества', max_length=200)
    slug = models.SlugField('Идентификатор сообщества в URL', unique=True)
    description = models.TextField('Описание сообщества')

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель публикаций"""

    text = models.TextField('Содержание поста')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Сообщество для публикации поста',
        blank=True, null=True
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Пост (публикация)'
        verbose_name_plural = 'Посты (публикации)'
        ordering = ('id',)


class Comment(models.Model):
    """Модель комментариев"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    """Модель подписок"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_follow',
            ),
        )
