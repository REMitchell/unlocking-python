from django.db import models


class TestModel(models.Model):
    some_name = models.CharField(max_length=32)
    some_number = models.IntegerField()
