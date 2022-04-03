from django.contrib import admin
from .models import User, Order, Product, Qna, Basket, ProductOption, OrderCount, Diary, Board, Comment, Like

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Qna)
admin.site.register(Basket)
admin.site.register(ProductOption)
admin.site.register(OrderCount)
admin.site.register(Diary)
admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(Like)


