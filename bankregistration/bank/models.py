from django.db import models
import uuid

# Create your models here.
Choices=[
    ('Thiruvanathapuram','tvm'),
    ('Ernakulam','ekm'),
    ('Calicut','clt'),
    ('wayanad','wyd'),
    ('kannur','knr')

]
class Districts(models.Model):
    name=models.CharField(max_length=100,unique=True,choices=Choices)
    slug=models.SlugField(max_length=100,unique=True)
    link=models.CharField(max_length=500,blank=True)
    class Meta:
        ordering=['name',]
        verbose_name='district'
        verbose_name_plural='districts'


    def __str__(self):
        return self.name


class Branch(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=199,unique=True)
    branch=models.ForeignKey(Districts,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

account_choices=[
    ('Savings Account','Savings Account'),
    ('Current Account','Current Account')
]

mat_choices=[
    ("Credit Card",'Credit Card'),
    ('Debit Card','Debit Card'),
    ('Pass Book','Pass Book')
]

gender_choice=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','other')
)


class Form(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,default=uuid.uuid1)
    dob=models.DateField(blank=True)
    age=models.IntegerField(blank=True)
    gender=models.CharField(max_length=200,choices=gender_choice)
    phonenumber=models.IntegerField(blank=True)
    mailid=models.EmailField(max_length=300,blank=True)
    address=models.TextField(max_length=200,blank=True)
    district=models.ForeignKey(Districts,on_delete=models.CASCADE)
    city=models.ForeignKey(Branch,on_delete=models.CASCADE)
    account=models.CharField(max_length=200,choices=account_choices)
    material=models.CharField(max_length=200,choices=mat_choices)

    class Meta:
        ordering=['name',]
        verbose_name='form'
        verbose_name_plural='forms'

    def __str(self):
        return  self.name


