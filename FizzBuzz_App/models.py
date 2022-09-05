from django.db import models

class FizzBuzz(models.Model):
    """
    Represents a single FizzBuzz object
    """
    fizzbuzz_id = models.AutoField(primary_key=True, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    useragent = models.TextField(null=True)
    message = models.TextField()