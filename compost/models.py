from django.db import models

class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    taken_at = models.DateTimeField(True)
