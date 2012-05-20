from django.db import models


class Article(models.Model):
    content = models.TextField()

    def __unicode__(self):
        return self.content


class Post(models.Model):
    article = models.ForeignKey(Article)
    content = models.TextField()

    def __unicode__(self):
        return self.content
