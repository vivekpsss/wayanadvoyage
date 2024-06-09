from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.name + " " + self.country + "-" + self.email

class Booking(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField()
    city= models.CharField(max_length=30)
    state= models.CharField(max_length=30)
    country= models.CharField(max_length=30)
    contact=models.BigIntegerField(max_length=20)
    pin=models.BigIntegerField(max_length=6)
    person=models.IntegerField()
    cin=models.DateField()
    cout=models.DateField()


class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  expiry=models.DateField('expiry',null=True)

  def is_expired(self):
      return timezone.now() > self.expiry