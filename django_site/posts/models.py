from django.db import models


class Tag(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField('Текст тега', max_length=255)

    def __str__(self):
        return self.text


class Post(models.Model):
    title = models.CharField('Название поста', max_length=255)
    author = models.CharField('Автор', max_length=255)
    original_id = models.CharField('id на сайте источника', max_length=255)
    pub_date = models.DateTimeField('Дата публикации')
    parse_date = models.DateTimeField('Дата парсинга', auto_now_add=True)
    origin = models.CharField('Источник', max_length=255)
    tags = models.ManyToManyField(Tag)
    text = models.TextField('Текст поста')

    def __str__(self):
        return self.title
