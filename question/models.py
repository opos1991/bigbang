from django.db import models

# Create your models here.


class Exam(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=10)

    def __str__(self):
        return self.answer
