from django.db import models

class FizzBuzz(models.Model):
    fizzbuzz_id = models.AutoField(primary_key=True, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    useragent = models.TextField()
    message = models.TextField()