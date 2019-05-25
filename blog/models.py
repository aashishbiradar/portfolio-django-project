from django.db import models
import time

class Blog(models.Model):
    urlkey = models.CharField(max_length=255, default=str(int(time.time())))
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:250]+ "..."

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e, %Y")
