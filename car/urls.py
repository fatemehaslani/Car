from django.urls import path
from . import views

urlpatterns = [

    path('welcome', views.welcome, name="welcome_page"),
    path('about', views.about, name="about_page"),
    path('car', views.car,),
    path('repre', views.repre, name="agents_page"),
    path('cars', views.car_list, name="cars_page"),
    path('cars/cancel', views.car_cancel, name="cancel_search"),
    path('sales', views.Car_sales, name="sales_page"),
    path('contact', views.contact_us, name="contact_page"),
    path('technical', views.technical, name="technical_page"),
    path('cars/repre', views.car_repre, name="car_create"),
    path('cars/<int:car_id>', views.car_detail, name="car_detail"),
    path('cars/cat/<int:cat_id>', views.car_list, name="cars_page_by_cat"),
    path('change/mode', views.change_mode, name="change_mode"),
    path('home', views.home, name="home"),
    path('api/cars', views.api_cars, name='api_cars'),
    path('api/car/<int:id>', views.api_car, name='api_car'),
]

