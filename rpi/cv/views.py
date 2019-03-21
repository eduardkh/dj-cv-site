from django.shortcuts import render


# Create your views here.
def Homepage(request):
    title = 'Homepage Title'
    context = {
        'title': title,
    }
    return render(request, 'index.html', context)
