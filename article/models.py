from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category',
    #                    args=[self.slug])


class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE,)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return self.name


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_app')
    category = models.ForeignKey(Subcategory, related_name='articlesubcategory', on_delete=models.CASCADE,)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # content = models.TextField(max_length=1000, blank=True, help_text='Enter the Article Short content ..........')
    summery = models.TextField(max_length=10000, blank=True, help_text='Enter the Article summery ..........')


    # class Meta:
    #     ordering = ['-created_on']

    def __str__(self):
        return self.title
