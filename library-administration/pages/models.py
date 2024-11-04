from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):

    status_val = [("avaliable", "avaliable"), ("rental", "rental"), ("sold", "sold")]
    title = models.CharField(max_length=20)
    auther = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rent_price = models.DecimalField(max_digits=7, decimal_places=2)
    rent_period = models.IntegerField()
    pages = models.IntegerField()
    active = models.BooleanField(default=True, null=True, blank=True)
    book_photo = models.ImageField(upload_to="photos", blank=True, null=True)
    author_photo = models.ImageField(upload_to="photos", blank=True, null=True)
    status = models.CharField(max_length=50, choices=status_val, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
