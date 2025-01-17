from django.contrib import admin
from .models import Car, Image, Equipment, Discount, User, Contact_us, Comment, Car_sales, Warranty_repairs, Sales_delivery, About_the_company, List_lottery_winners, Technical_specifications, Representation, Category, Tag, Slider

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'price', 'color', 'category')
    list_filter = ('category',)
    list_per_page = 1

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'visibility')


   # def aa(self.Comment):
    #    if int(Comment.like_count) > 5 :
     #       return "Good"
      #  else:
       #     return "Bad"

admin.site.register(Car, CarAdmin)
admin.site.register(Image)
admin.site.register(Equipment)
admin.site.register(Discount)
admin.site.register(User)
admin.site.register(Contact_us)
admin.site.register(Comment)
admin.site.register(Car_sales)
admin.site.register(Warranty_repairs)
admin.site.register(Sales_delivery)
admin.site.register(About_the_company)
admin.site.register(List_lottery_winners)
admin.site.register(Technical_specifications)
admin.site.register(Representation)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Slider)

