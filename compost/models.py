from django.db import models

class Measure(models.Model):
    temperature = models.DecimalField(max_digits=2, decimal_places=2)
    taken_at = models.DateTimeField(True)
