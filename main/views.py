from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'title': 'Home',
        'content': 'Logorithm: everything you\'ve ever thought about'
    }


    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About',
        'content': 'About us',
        'text_on_page': '''
                        Sun of the sleepless! Melancholy star!
                        Whose tearful beam glows tremulously far,
                        That show’st the darkness thou canst not dispel,
                        How like art thou to joy remember’d well!

                        So gleams the past, the light of other days,
                        Which shines, but warms not with its powerless rays;
                        A night-beam Sorrow watcheth to behold,
                        Distinct, but distant — clear, but oh, how cold!
                        '''
            }


    return render(request, 'main/about.html', context)