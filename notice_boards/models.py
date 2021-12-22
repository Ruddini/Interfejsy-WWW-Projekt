from django.db import models

class Topic(models.Model):
    """Topic of Notices Class """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Representation Model as a text"""
        return self.text

class Notice(models.Model):
    """Notice Class"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'notices'

    def __str__(self):
        """Representation Model as a text"""
        return f"{self.text[:50]}..."