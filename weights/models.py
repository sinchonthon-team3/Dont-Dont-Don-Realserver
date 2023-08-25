from django.db import models


class Weight(models.Model):
    weight_name = models.CharField(max_length=20)
    is_travel = models.BooleanField()
    amount = models.IntegerField()
