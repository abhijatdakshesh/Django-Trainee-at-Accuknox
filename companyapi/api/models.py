from django.db import models

# Create your models here.
# Creating Company Models
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 50)
    localtion = models.CharField(max_length=100)
    about= models.TextField()
    type = models.CharField(max_length=100, choices=
                            (('IT', 'IT'), 
                             ('Account', 'Account'), 
                             ('HR', 'HR')
                             ))
    added_dates = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + self.localtion

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=
                                (('manager', 'manager'), 
                                 ('software developer', 'SD'),
                                 ('Team Lead', 'TL')
                                 ))
    company= models.ForeignKey(Company, on_delete=models.CASCADE)
