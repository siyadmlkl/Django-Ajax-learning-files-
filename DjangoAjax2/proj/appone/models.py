from django.db import models


class Assets(models.Model):
    area = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    asset = models.CharField(max_length=100, default="Unit")

    def __str__(self):
        return str(self.area) + '|' + str(self.location)
