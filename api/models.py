from django.db import models
from django.core.exceptions import ValidationError

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Songs(models.Model):
    title = models.CharField(max_length=250)
    duration_minutes = models.PositiveIntegerField()
    duration_seconds = models.PositiveIntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)

    def __str__(self):
        singer_name = self.singer.name if self.singer else "No Singer"
        return f"{self.title} - {singer_name}"

    def get_duration_display(self):
        return f"{self.duration_minutes}:{self.duration_seconds:02d}"

    def clean(self):
        if self.duration_seconds >= 60:
            raise ValidationError("Seconds must be less than 60")
