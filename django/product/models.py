from django.db import models


class ProductModels(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'Products'


class UserModel(models.Model):
    pass
