from django.shortcuts import render
from .models import Concert
from datetime import date

def concert_list(request):
    # Crear conciertos de ejemplo si no existen
    if Concert.objects.count() == 0:
        Concert.objects.create(
            band="The Rock Stars",
            venue="Estadio Nacional",
            city="Santiago",
            date=date(2024, 4, 15),
            price=45.00
        )
        Concert.objects.create(
            band="The Rock Stars",
            venue="Teatro Colón",
            city="Buenos Aires",
            date=date(2024, 5, 22),
            price=55.00
        )
        Concert.objects.create(
            band="The Rock Stars",
            venue="Movistar Arena",
            city="Bogotá",
            date=date(2024, 6, 10),
            price=38.00
        )
    
    concerts = Concert.objects.all().order_by('date')
    return render(request, 'concerts/concert_list.html', {'concerts': concerts})
