from django.db import models


# Create your models here.

class Car_sales(models.Model):
    customer_service_desk = models.CharField(max_length=200, null=True, blank=True)
    sale_delivery_information = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)

class Category(models.Model):
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Car(models.Model):
    car_name = models.CharField(max_length=250)
    color = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to="cars", null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    #main_pic = models.CharField(max_length=200, null=False, blank=True)
    model_car = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    published_date = models.DateTimeField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    Discount = models.ManyToManyField('Discount', related_name='cars_discount')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    tags = models.ManyToManyField('Tag', related_name='tags')
    Technical_specifications = models.ManyToManyField('Technical_specifications', related_name='cars_spec')
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=False)



    def __str__(self):
        return self.car_name


class Image(models.Model):
    file_image = models.CharField(max_length=250)
    title_image = models.CharField(max_length=250, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=None, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)


class Equipment(models.Model):
    brake = models.CharField(max_length=250)
    the_light = models.CharField(max_length=200, null=True, blank=True)
    mirrors = models.CharField(max_length=200, null=True, blank=True)
    command = models.CharField(max_length=200, null=True, blank=True)
    safety_equipment = models.CharField(max_length=200, null=True, blank=True)
    rims_tires = models.CharField(max_length=250, null=True, blank=True)
    chair = models.CharField(max_length=200, null=True, blank=True)
    the_glasses = models.CharField(max_length=200, null=True, blank=True)
    sound_system = models.CharField(max_length=200, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=None, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)


class Discount(models.Model):
    discount_percent = models.CharField(max_length=200, null=True, blank=True)
    discount_code = models.CharField(max_length=250, null=True, blank=True)
    datetime_start = models.DateTimeField(null=True, blank=True)
    datetime_end = models.DateTimeField(null=True, blank=True)


class User(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    national_code = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=11, null=True, blank=True)
    password = models.CharField(max_length=500, null=True, blank=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)


class Contact_us(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=255, null=True, blank=True)
    mailbox = models.CharField(max_length=255, null=True, blank=True)  #صندوق پستی
    E_mail = models.EmailField(max_length=255, null=True, blank=True)   # پست الکترونیکی
    direct_communication = models.CharField(max_length=255, null=True, blank=True)  #ارتباط مستقیم
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)


class Comment(models.Model):
    class Visibility(models.TextChoices):
        VISIBLE = 'VI', 'VISIBLE'
        INVISIBLE = 'IN', 'INVISIBLE'

    content = models.TextField(null=True, blank=True)
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()
    #report = models.CharField(max_length=100)
    replay = models.TextField(null=True, blank=True)
    publish_date = models.DateField(null=True, blank=True)
    visibility = models.CharField(choices=Visibility, default=Visibility.INVISIBLE, max_length=2)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    user_admin = models.CharField(max_length=250, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=None, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=None, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class Warranty_repairs(models.Model):
    text = models.TextField()
    scope_service = models.CharField(max_length=255, null=True, blank=True)
    service_delivery_method = models.CharField(max_length=255, null=True, blank=True)
    required_documents = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(null=True, decimal_places=0, max_digits=20)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    sales = models.ForeignKey(Car_sales, on_delete=models.RESTRICT, default=None, null=True)

class Sales_delivery(models.Model):
    customer_service_desk = models.CharField(max_length=255, null=True, blank=True)
    vehicle_documents = models.CharField(max_length=255, null=True, blank=True)
    payment = models.DecimalField(null=True, decimal_places=0, max_digits=20)
    debt_settlement = models.CharField(max_length=255, null=True, blank=True)
    sales_invoice = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)


class About_the_company(models.Model):
    body = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)

class List_lottery_winners(models.Model):
    title = models.CharField(max_length=400, null=True, blank=True)
    tracking_number = models.IntegerField()
    users = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    sale = models.ForeignKey(Car_sales, on_delete=models.CASCADE, default=None)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)

class Technical_specifications(models.Model):  #مشخصات فنی
    title = models.CharField(max_length=700, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=None)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)

    def __str__(self):
        return self.title


class Representation(models.Model):
   # class Status(models.TextChoices):
    #    DRAFT = 'DF', 'DRAFT'
     #   PENDING = 'PN', 'PENDING'
      #  PUBLISHED = 'PF', 'PUBLISHED'
    STATUES = {
        ("DF", "DRAFT"),
        ("PN", "PENDING"),
        ("PF", "PUBLISHED")
    }
    province = models.CharField(max_length=250, null=True, blank=True)
    agent_code = models.CharField(max_length=250, null=True, blank=True)   #کد نمایندگی
    city = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField()
    regional_office = models.CharField(max_length=255, null=True, blank=True)  #دفتر منطقه ای
    managers_name = models.CharField(max_length=255, null=True, blank=True)   #نام مدیر
    sales_areas = models.CharField(max_length=255, null=True, blank=True)    #مناطق فروش
    status = models.CharField(choices=STATUES, max_length=2)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)

class Stocks_investors(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_date = models.DateTimeField(auto_now_add=True, null=True, editable=False)

class Slider(models.Model):
    file = models.FileField(upload_to="sliders")
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

