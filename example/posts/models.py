from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        verbose_name = u"Category"
        verbose_name_plural = u"Categories"

    def __unicode__(self):
        return u'%s' % self.id


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __unicode__(self):
        return u'%s' % self.id

    @models.permalink
    def get_absolute_url(self):
        return 'post-detail', (self.id,)
