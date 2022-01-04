from django.db import models
from django.contrib.auth.models import User

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
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'notices'

    def __str__(self):
        """Representation Model as a text"""
        return f"{self.text[:50]}..."