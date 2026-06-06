from django.db import models


# Create your models here.
    
class Member(models.Model):
    Email = models.EmailField(max_length=60, unique=True)
    Name = models.CharField(max_length=30, unique=True)
    Emp_Id = models.CharField(max_length=9, primary_key=True)
    Job = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Contact = models.IntegerField(null=False)
    Account = models.CharField(max_length=30, null=False)
    Salary = models.IntegerField(null=False)
    Start_Date = models.DateField(null=False)
    company_name = models.CharField(max_length=30, null=True)
    Admin_Password = models.CharField(max_length=30, null=True)
    Announcements = models.TextField()
    Complaints = models.TextField()
    Leaves = models.TextField()

    class Meta:
        db_table = 'emp_table'
        managed = False

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = 'Emp_Id'

    def __str__(self):
        return self.Email