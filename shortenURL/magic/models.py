from django.db import models


class ShortenURL(models.Model):
    shortenURL = models.CharField(primary_key=True, db_index=True, max_length=64)
    originURL = models.CharField(max_length=256)

    visited = models.IntegerField(default=0)
