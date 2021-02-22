from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name

class ContactInformation(models.Model):
    address = models.CharField(max_length = 300)
    tole = models.CharField(max_length = 300)
    contact_no = models.CharField(max_length = 300)
    time = models.CharField(max_length = 300)
    email = models.CharField(max_length = 300)

    def __str__(self):
        return self.address

class Testonomial(models.Model):
    name = models.CharField(max_length = 300)
    post = models.CharField(max_length = 300)
    comment = models.TextField()
    image = models.TextField(max_length = 300)


    def __str__(self):
        return self.name