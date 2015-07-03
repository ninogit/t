from django.db import models

# Create your models here.

class Shop(models.Model):
    url = models.URLField(unique=True)
    description = models.TextField( blank=True, null=True)
    desc = ['CMS','jgsgj']

    class Meta:
        ordering = ['pk']
