from django.shortcuts import render
from .models import Photo

def photo_list(request):
    # Crear algunas fotos de ejemplo si no existen
    if Photo.objects.count() == 0:
        Photo.objects.create(
            title="Concierto en Vivo 2024",
            image_url="https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?w=800",
            description="Nuestro concierto más reciente en el estadio principal. Una noche mágica llena de música y energía."
        )
        Photo.objects.create(
            title="Grabación en Estudio",
            image_url="https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=800",
            description="En el estudio de grabación trabajando en nuestro nuevo álbum."
        )
        Photo.objects.create(
            title="Encuentro con Fans",
            image_url="https://images.unsplash.com/photo-1501612780327-45045538702b?w=800",
            description="Compartiendo momentos especiales con nuestros fans después del concierto."
        )
    
    photos = Photo.objects.all()
    return render(request, 'photos/photo_list.html', {'photos': photos})