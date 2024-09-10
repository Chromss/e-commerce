from django.shortcuts import render

def show_main(request):
    context = {
        'app': 'HomifyInc',
        'name': 'Nabil Zahid Rahman',
        'class': 'PBP-A'
    }

    return render(request, "main.html", context)