from django.db import models

# Create your models here.
class books(models.Model):
    book_name = models.CharField(max_length=20)
    add_data = models.DateField()
    author = models.CharField(max_length=20)
    public = models.CharField(max_length=20)
    get_times = models.IntegerField()
    is_borrow = models.BooleanField(default=False)
    def __str__(self):
        return self.book_name

class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sex = models.BooleanField(default=False)
    age = models.IntegerField()
    def __str__(self):
        return self.username

class borrow_record(models.Model):
    book = models.ForeignKey('books',on_delete=models.CASCADE)
    user = models.ForeignKey('user',on_delete=models.CASCADE)
    borDate = models.DateField()
    deadline = models.IntegerField()
