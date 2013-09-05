from django.db import models
from django.contrib import admin
# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()
	# **def __unicode__(self):**
	# 	**return self.name**

class Author(models.Model):
	"""docstring for Author"""
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	# ** def __unicode__(self):**
	# 	**return u'%s %s' % (self.first_name, self.last_name)**

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()
	# **def __unicode__(self):**
	# 	**return self.title**

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)