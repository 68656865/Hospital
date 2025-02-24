from django.db import models
class Registration(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField(null=True,blank=True)
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=200)
    Phone=models.TextField()
    Catagory=models.CharField(max_length=50,null=True,blank=True)

class Doctor(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField(null=True,blank=True)
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=200)
    Phone=models.TextField()
    Catagory=models.CharField(max_length=50,null=True,blank=True)
    Address=models.TextField(null=True,blank=True)
    Department=models.TextField(null=True,blank=True)


class Staff(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField(null=True,blank=True)
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=200)
    Phone=models.TextField()
    Catagory=models.CharField(max_length=50,null=True,blank=True)
    Address=models.TextField(null=True,blank=True)
    Department=models.TextField(null=True,blank=True)

class Patients(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField(null=True,blank=True)
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=200)
    Phone=models.TextField()
    Catagory=models.CharField(max_length=50,null=True,blank=True)
    Address=models.TextField(null=True,blank=True)
    Department=models.TextField(null=True,blank=True)

class Booking(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField(null=True,blank=True)
    Username=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=200)
    Phone=models.TextField()
    Catagory=models.CharField(max_length=50,null=True,blank=True)
    Address=models.TextField(null=True,blank=True)
    Department=models.TextField(null=True,blank=True)
    Tocken=models.IntegerField(null=True,blank=True)




    

    
    


