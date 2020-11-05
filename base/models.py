from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from ckeditor.fields import RichTextField
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Product(models.Model):
	free = models.BooleanField(blank=True, null=True)
	title = models.CharField(max_length=120, null=True)

	cover_image= ProcessedImageField(upload_to='cover',blank=False,null=True,
									  processors=[ResizeToFill(1280, 720)],
									  format='JPEG',
									  )
	description = models.TextField(null=True)
	price = models.FloatField(null=True, blank=True)

	students = models.ManyToManyField(User,
	                                    related_name='courses_joined',
	                                    blank=True)
	def __str__(self):
		return self.title
	@property
	def lessons(self):
	    return self.lesson_set.all().order_by('position')

class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    content = RichTextField(null=True)
    position = models.IntegerField()


    def __str__(self):
        return self.title


    



class Order(models.Model):
	product = models.ForeignKey(Product, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 
	
	def __str__(self):
		return self.product.name




