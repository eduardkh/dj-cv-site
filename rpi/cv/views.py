from django.shortcuts import render
from datetime import date

birthDay = date(1984,3,1)


def calculate_age(birthDay):
    today = date.today()
    return today.year - birthDay.year - ((today.month, today.day) < (birthDay.month, birthDay.day))


# Create your views here.
def Homepage(request):
    title = 'Full-stack Web Developer and Network Engineer CV'
    name = 'Eduard Khiaev'
    age = calculate_age(birthDay)
    country = 'Israel'
    location = 'Rishon Le-Tsiyon'
    eMail = 'eddietheone1984@gmail.com'
    phone = '052-4712148'
    freelance = 'Soon'

    context = {
        'title': title,
        'name': name,
        'age': age,
        'country': country,
        'location': location,
        'eMail': eMail,
        'phone': phone,
        'freelance': freelance,
    }
    return render(request, 'index.html', context)
