from django.shortcuts import render
from .models import Song

def song_list(request):
    # Crear algunas canciones de ejemplo si no existen
    if Song.objects.count() == 0:
        Song.objects.create(
            title="Bohemian Rhapsody",
            artist="Queen",
            album="A Night at the Opera",
            year=1975,
            lyrics="Is this the real life? Is this just fantasy? Caught in a landslide, No escape from reality..."
        )
        Song.objects.create(
            title="Hotel California",
            artist="Eagles",
            album="Hotel California",
            year=1977,
            lyrics="On a dark desert highway, cool wind in my hair, Warm smell of colitas, rising up through the air..."
        )
        Song.objects.create(
            title="Stairway to Heaven",
            artist="Led Zeppelin",
            album="Led Zeppelin IV",
            year=1971,
            lyrics="There's a lady who's sure all that glitters is gold, And she's buying a stairway to heaven..."
        )
    
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})