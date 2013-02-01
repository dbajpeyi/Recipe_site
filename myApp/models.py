from django.db import models
import datetime

# Create your models here.
class Recipe(models.Model):
	title = models.CharField(max_length=100)
	ingredients = models.TextField(max_length=200,help_text="Put the ingredients required for the recepies here !")
	instructions = models.TextField(max_length=500)
	#slug = models.SlugField(max_length=100,unique=True)
	#posted_on = models.DateTimeField('Posted On')

	def __unicode__(self):
		return self.title

 
