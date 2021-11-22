from django.shortcuts import render



family = ['Иванов', 'Петров', 'Сидоров']
def index(request):
    name = 'Ivanov'
    langs = ["English", "German", "French", "Spanish", "Chinese"]
    return render(request, 'index.html', context= {'langs': langs, 'family': family, 'name':name})



