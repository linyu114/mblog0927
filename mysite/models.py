from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True) #自動取得現在時間
    
    class Meta:
        ordering = ('-pub_date',) #用pub_date去排序 -反向排序
    
    def __str__(self):
        return self.title #印出標題就好
    
class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES) #choices會幫忙做成選單
    #result = models.BooleanField()#BooleanField->勾選方塊