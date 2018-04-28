from django.db import models


# Create your models here.


class Topic(models.Model):
    """Learning topic"""
    text = models.CharField(max_length=250)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the model"""
        return self.text


class Entry(models.Model):
    """Entry of specific topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """String representation of the model"""
        return self.text[:50] + '...'
