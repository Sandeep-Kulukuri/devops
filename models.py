from django.db import models


# Create your models here.
class Reg(models.Model):
    email = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)

    def _str_(self):
        return self.email

class Subject(models.Model):
    sub_name = models.CharField(max_length=30)
    sub_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.sub_name
'''

class Subdomain(models.Model):
    domain_name = models.CharField(max_length=30)
    sub_name=models.CharField(max_length=30)

    def __str__(self):
        return self.domain_name,self.sub_name
'''


class Questions(models.Model):
    sub_name=models.CharField(max_length=50)
    marks=models.CharField(max_length=10)
    question=models.CharField(max_length=100)
    option1=models.CharField(max_length=50)
    option2=models.CharField(max_length=50)
    option3=models.CharField(max_length=50)
    option4=models.CharField(max_length=50)
    answer=models.CharField(max_length=50)
    def __str__(self):
        return self.sub_name
class Enrollment(models.Model):
    sub_name=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    def __str__(self):
        return self.email
class Marks(models.Model):
    email=models.CharField(max_length=50)
    sub_name=models.CharField(max_length=50)
    marksvalue=models.CharField(max_length=10)
    marks=models.CharField(max_length=10)
    def __str__(self):
        return self.email