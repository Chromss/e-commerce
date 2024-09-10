from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306203324',
        'name': 'Nabil Zahid Rahman',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)