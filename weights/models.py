from django.db import models


class Weight(models.Model):
    weight_name = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)
