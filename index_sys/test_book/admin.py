from django.contrib import admin
from test_book.models import books,user,borrow_record
# Register your models here.
admin.site.register(books)
admin.site.register(user)
admin.site.register(borrow_record)