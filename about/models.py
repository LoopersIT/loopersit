from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ['order']


