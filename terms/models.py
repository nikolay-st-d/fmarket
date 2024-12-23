from django.db import models


class Term(models.Model):
    title = models.CharField(
        max_length=255,
    )
    content = models.TextField()
    last_updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title
