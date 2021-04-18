from django.db import models

# Create your models here.
class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=255)
  age = models.IntegerField()

  def __str__(self):
    return self.name 

  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'dog_id': self.id})