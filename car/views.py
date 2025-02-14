from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response
from . import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
from .models import *
from .forms import CarForm
from .serializers import CarSerializer
# Create your views here.

def home(request):
    request.session["page_route_name"] = "home"
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    sliders = Slider.objects.all()
    return render(request, 'welcome.html', context={'sliders': sliders, 'mode': mode})

def car_cancel(request):
    if 'query' in request.session and request.session['query']:
        del request.session['query']
    return HttpResponseRedirect(reverse('cars_page'))

def car_list(request, cat_id=None):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('auth_login'))

    request.session["page_route_name"] = "cars_page"
    query = request.GET.get('query', None)

    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    if cat_id:
        cars = Car.objects.filter(is_approved=True).filter(category=cat_id).order_by('-published_date')
    elif query:
        request.session['query'] = query

        q = Q(car_name__icontains=query) | Q(description__icontains=query)
        cars = Car.objects.filter(q).order_by('-id')
    elif 'query' in request.session and request.session['query'] is not None:
        old_query = request.session['query']
        q = Q(car_name__icontains=old_query) | Q(description__icontains=old_query)
        cars = Car.objects.filter(q).order_by('-id')
    else:
        cars = Car.objects.filter(is_approved=True).order_by('-published_date')

    categories = Category.objects.all()

    paginator = Paginator(cars, 3)

    page_number = request.GET.get("p", 1)

    cars_with_paginaton = paginator .get_page(page_number)

    return render(request, 'cars.html', context={'cars': cars_with_paginaton, 'categories': categories, 'mode': mode})

def car_detail(request, car_id):
    request.session["page_route_name"] = "car_detail"
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

    sliders = Slider.objects.all()
    car = Car.objects.filter(pk=car_id).first()
    tags = car.tags.all()
    technicals = Technical_specifications.objects.filter(car=car_id).order_by('-created_date')
    comments = Comment.objects.filter(car=car_id).filter(visibility='VI').order_by('-created_date')
    return render(request, 'car.html', context={'car': car, 'all_technicals': technicals, 'all_tags': tags, 'sliders': sliders, 'all_comments': comments, 'mode':mode})

def welcome(request):
    request.session["page_route_name"] = "welcome_page"
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']

   # context = {
     #   'user_name': "Dear user",
      #  'is_admin': False,
      #  'skill': ["ww","eee"],
    #}
    sliders = Slider.objects.all()
    return render(request, template_name='welcome.html', context={'sliders': sliders, 'mode': mode})
   # return HttpResponse("Welcome to my car")

def about(request):
    request.session["page_route_name"] = "about_page"
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']
    return render(request, template_name='about.html', context={'mode': mode})
    #return HttpResponse("About us")

def car(request):
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']
    categories = Category.objects.all()
    return render(request, template_name='car.html', context={'categories': categories, 'mode': mode})

def repre(request):
    request.session["page_route_name"] = "agents_page"
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']
    return render(request, template_name='Representation.html', context={'mode': mode})


def Car_sales(request):
    request.session["page_route_name"] = "sales_page"
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']
    return render(request, template_name='sales.html', context={'mode': mode})

def contact_us(request):
    request.session["page_route_name"] = "contact_page"
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']
    return render(request, template_name='contact.html', context={'mode': mode})

def technical(request):
    request.session["page_route_name"] = "technical_page"
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']
    technical = Technical_specifications.objects.all()

    return render(request, template_name='technical.html', context={'technicals': technical, 'mode': mode})


def car_repre(request):
    request.session["page_route_name"] = "car_create"
    if 'mode' not in request.session:
        request.session['mode'] = 'dark'
        mode = request.session['mode']
    else:
        mode = request.session['mode']
    if request.method == "REPRE":
        form = CarForm(request.REPRE)
        if form.is_valid():
            car = form.save(commit=True)
            return HttpResponseRedirect(reverse('agents_page'))
        else:
            return HttpResponse("No valid data")
    else:
        form = CarForm()
        return render(request, template_name='car_repre.html', context={'form': form, 'mode': mode})


def change_mode(request):
    if 'mode' in request.session:
        if request.session.get('mode') == 'dark':
            request.session['mode'] = 'light'
        else:
            request.session['mode'] = 'dark'
    else:
        request.session['mode'] = 'dark'

    page = request.session.get('page_route_name')
    return HttpResponseRedirect(reverse(page))

#API
@api_view(['GET', 'POST'])
def api_cars(request):
    if request.method == 'GET':
        cars = Car.objects.select_related('category').filter(is_approved=True).order_by('-published_date')
        serialized_cars = CarSerializer(cars, many=True)
        return Response(serialized_cars.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = CarSerializer(data=request.data)
        #print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def api_car(request, id):
    car = get_object_or_404(Car, pk=id)

    if request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "message": "بروزرسانی با موفقیت انجام شد"
            }, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        # check file exist or not
        if car.file is not None:
            return Response({
                "message": "انجام این عمل به دلیل داشتن عکس امکان پذیر نیست!"
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        # tags
        if car.tags.count() > 0:
            return Response({
                "message": "انجام این عمل امکان پذیر نیست!"
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
       # car.delete()
        return Response({
            "message": "حذف اطلاعات با موفقیت انجام شد"
        }, status=status.HTTP_204_NO_CONTENT)
    serialized_car = CarSerializer(car)
    return Response(serialized_car.data)
    #try:
      #  car = Car.objects.get(pk=id)
     #   serialized_car = CarSerializer(car)
    #    return Response(serialized_car.data)
   # except Car.DoesNotExist:
    #    return Response(status=404)

