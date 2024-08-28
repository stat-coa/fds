from django.shortcuts import render, redirect
from .models import Year, IndustryCrossPrimary, Marketing, Industry, Primary
from pprint import pprint


# Create your views here.
def home(request):
    year = Year.objects.order_by('-Year').first()
    print(f"X-Reapl_IP: {request.headers.get('X-Real-IP')}")
    # print(f"headers: {request.headers}")
    print(f"request.META['REMOTE_ADDR'] = {request.META['REMOTE_ADDR']}")
    # pprint(f"request.META = {request.META}")

    return render(request, "home.html", context={
        'objects': {'latestPriodData': year, 'nextPeriodData': year.Year + 5, 'nextDataReleasedTime': year.Year + 8}})


def background(request):
    return render(request, "background.html")


def glossary(request):
    return render(request, 'glossary.html')


def download(request):
    return render(request, 'download.html')


def documentation(request):
    year = Year.objects.order_by('-Year').first()
    marketing = Marketing.objects.filter(Sector__Name="整體農食", Year=year).first()
    industry = Industry.objects.filter(Sector__Name="整體農食", Year=year).first()
    primary = Primary.objects.filter(Sector__Name="整體農食", Year=year).first()
    cross_table = IndustryCrossPrimary.objects.all()
    # return render(request, "documentation.html", context = {'objects':{'year': year,'nextPeriodData':year.year+5,
    #                                                                    'cross_table': cross_table,}})
    return render(request, "documentation.html", context={'objects': {'year': year, 'nextPeriodData': year.Year + 5},
                                                          'marketing_data': marketing,
                                                          'industry_data': industry,
                                                          'primary_data': primary,
                                                          'table_data': cross_table, })


def quickfacts(request):
    return render(request, "quickfact.html")


def catch_all(request):
    return redirect("home")

