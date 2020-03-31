from django.core.checks import register
from django.db import models


class SimpleModel(models.Model):
    field = models.IntegerField()
    manager = models.manager.Manager()


class CheckModel(models.Model):
    pass


@register('tests')
def my_check(app_configs, **kwargs):
    CheckModel.objects.create()
    return []


my_check.did_run = False
