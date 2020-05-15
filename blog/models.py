from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    # body를 첫 글자부터 100글자까지 자름
    def summary(self):
        return self.body[:100]
