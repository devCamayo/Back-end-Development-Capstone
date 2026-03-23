from django.shortcuts import render

def home(request):
    context = {
        'band_name': 'The Rock Stars',
        'band_description': 'Somos una banda de rock formada en 2020, dedicada a crear música que inspire y conecte con las emociones más profundas.',
        'band_members': [
            {'name': 'John Smith', 'instrument': 'Voz y Guitarra'},
            {'name': 'Maria Garcia', 'instrument': 'Bajo'},
            {'name': 'David Lee', 'instrument': 'Batería'},
            {'name': 'Anna Brown', 'instrument': 'Teclados'},
        ],
        'band_history': 'Nuestra historia comenzó en un pequeño garaje, tocando covers de nuestras bandas favoritas. Con el tiempo, desarrollamos nuestro propio sonido único que mezcla rock clásico con toques modernos.',
    }
    return render(request, 'home.html', context)