from django.db import models

class Day(models.Model):
    date = models.DateField(unique=True)
    image_filename = models.CharField(max_length=100)  # e.g., "2025-02-25.jpg"

    def __str__(self):
        return str(self.date)
