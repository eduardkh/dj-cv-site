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
    experienceTitle1 = 'Technical Support Call Center - Bezeq'
    experienceDate1 = 'Dec 2008 - May 2014'
    experiencText1 = '''
Managed, maintained all major circuits and infrastructures that service client networks, and performed troubleshooting as necessary.
    '''
    experienceTitle2 = 'Communication and Security Analyst - Metropolinet'
    experienceDate2 = 'Sep 2014 - Mar 2017'
    experiencText2 = '''
Developed protocol for downtime, accessibility issues and other common concerns faced by the company and IT department.
Lead IT initiatives to improve network accessibility, minimized downtime and implemented solutions to common issues.
Supervised all team members working on IT system, and provided training and corrective action whenever necessary.
    '''
    experienceTitle3 = 'Network Engineer - Isracard'
    experienceDate3 = 'Mar 2017 - Present'
    experiencText3 = '''
Communicate with clients and internal contacts to improve efficacy of the server and its networks.
Implement software and hardware that facilitates access to network and improves client experience.
Switch and route servers as needed to troubleshoot and maintain satisfactory level of service.
    '''

    context = {
        'title': title,
        'name': name,
        'age': age,
        'country': country,
        'location': location,
        'eMail': eMail,
        'phone': phone,
        'freelance': freelance,
        'experienceTitle1': experienceTitle1,
        'experienceDate1': experienceDate1,
        'experiencText1': experiencText1,
        'experienceTitle2': experienceTitle2,
        'experienceDate2': experienceDate2,
        'experiencText2': experiencText2,
        'experienceTitle3': experienceTitle3,
        'experienceDate3': experienceDate3,
        'experiencText3': experiencText3,
    }
    return render(request, 'index.html', context)
