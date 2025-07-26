from django.db import models
from django.contrib.postgres.fields import JSONField

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    fields = models.JSONField()

    def __str__(self):
        return self.formNumber
