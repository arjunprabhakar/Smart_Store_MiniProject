from email.policy import default
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.signals import pre_save
from smartstore.utils import unique_slug_generator


# Create your models here.

#Category Table
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,null=True,blank=True,editable=False)
    description=models.TextField(blank=True)
    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return  '{}' .format(self.name)

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Category)


#Product Table
class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True,editable=False)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return  '{}' .format(self.name)
def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Product)