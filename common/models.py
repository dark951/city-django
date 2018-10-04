from django.db import models


class Timestamped(models.Model):
    """
    Abstract model that adds created and modified at fields, for notice time of add and time of modify row
    """
    created_at = models.DateTimeField('Utworzony', auto_now_add=True)
    modified_at = models.DateTimeField('Zmodyfikowany', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True
