from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Songs(models.Model):
    title = models.CharField(max_length=250)
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)

    def __str__(self):
        return self.title
