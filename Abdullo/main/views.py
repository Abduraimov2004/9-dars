from django.shortcuts import render
from .models import Car, Brand, Color


def car_list(request):
    selected_brand = request.GET.get('brand')
    selected_color = request.GET.get('color')

    cars = Car.objects.all()

    if selected_brand:
        cars = cars.filter(brand_id=selected_brand)

    if selected_color:
        cars = cars.filter(color_id=selected_color)

    brands = Brand.objects.all()
    colors = Color.objects.all()

    context = {
        'cars': cars,
        'brands': brands,
        'colors': colors,
        'selected_brand': selected_brand,
        'selected_color': selected_color,
    }

    return render(request, 'car_list.html', context)
