from django.db import models

# Create your models here.


class RegisterTable(models.Model):
    firstname=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
        


class ProfileUser(models.Model):
    user=models.ForeignKey(RegisterTable,on_delete=models.CASCADE,null=True)
    forget_pass_token=models.CharField(max_length=300)
    create_at=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.email       