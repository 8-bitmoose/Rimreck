from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def animals(request):
    return render(request, "pages/animals.html")


def scan(request):
    return render(request, "pages/scan.html")


def reports(request):
    return render(request, "pages/reports.html")
