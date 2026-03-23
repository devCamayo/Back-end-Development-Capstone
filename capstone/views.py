from django.shortcuts import render

def home(request):
    context = {
        'band_name': 'Djirection',
        'band_description': 'A British-Irish band formed in 2023, bringing you the best of rock and alternative music.',
        'band_members': [
            {'name': 'James O\'Connor', 'instrument': 'Lead Vocals & Guitar'},
            {'name': 'Liam Murphy', 'instrument': 'Lead Guitar & Backing Vocals'},
            {'name': 'Thomas Walsh', 'instrument': 'Bass Guitar'},
            {'name': 'Daniel Byrne', 'instrument': 'Drums & Percussion'},
        ],
        'band_history': 'Djirection is a British-Irish rock band formed in London in 2023. The band consists of four talented musicians who came together with a shared vision of creating music that transcends boundaries.',
        'achievements': [
            'Best New Artist - British Music Awards 2023',
            'Debut Album "New Horizons" reached #1 on UK Rock Charts',
            'Sold-out debut tour across UK and Ireland',
            'Nominated for Best Rock Album at the 2024 Brit Awards',
            'Featured in Rolling Stone Magazine as "Ones to Watch"'
        ]
    }
    return render(request, 'home.html', context)

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')