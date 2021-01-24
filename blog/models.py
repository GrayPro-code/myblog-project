from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=300)
	image = models.ImageField(upload_to='event_images/')
	text = models.TextField()
	date = models.DateTimeField()
	
	def get_summery(self):
		return self.text[:56]


	def __str__(self):
		return self.title



