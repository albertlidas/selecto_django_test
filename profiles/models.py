from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, db_index=True)
    phone = models.CharField(max_length=100, db_index=True)
    address = models.CharField(max_length=100, db_index=True)
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __unicode__(self):
        return u"{} {}".format(self.first_name, self.last_name)

    def last_comment(self):
        if Comment.objects.filter(receiver__id=self.id):
            return Comment.objects.filter(receiver__id=self.id)[0]
        else:
            return u"No Comments"

    def comments_count(self):
        return Comment.objects.filter(receiver__id=self.id).count()

class Comment(models.Model):
    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    author = models.CharField(max_length=2000, db_index=True)
    text = models.CharField(max_length=2000, db_index=True)
    rating = models.CharField(max_length=1, choices=CHOICES)
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)
    receiver = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.author)
