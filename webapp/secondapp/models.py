from django.db import models


# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    title=models.CharField(max_length=250,verbose_name='Заголовок')
    slug=models.SlugField(verbose_name='URL',unique=True,db_index=True)
    content=models.TextField(verbose_name='Контент')
    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    time_update=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null=True,verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(verbose_name='URL', unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

