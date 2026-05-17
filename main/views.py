from django.shortcuts import render


def home(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def job_apply(request):
    return render(request, 'job_apply.html')

