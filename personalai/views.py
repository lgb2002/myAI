from django.shortcuts import render
from django.utils import timezone

def introduce(request):
    return render(request, 'personalai/index.html', {})

def location(request):
    return render(request, 'personalai/location.html', {})
def device(request):
    return render(request, 'personalai/device.html', {})
def personal(request):
    return render(request, 'personalai/personal.html', {})
def financial(request):
    return render(request, 'personalai/financial.html', {})
def health(request):
    return render(request, 'personalai/health.html', {})
def browsing(request):
    return render(request, 'personalai/browsing.html', {})

def btns_1(request):
    return render(request, 'personalai/btns_1.html', {})

def btns_2(request):
    return render(request, 'personalai/btns_2.html', {})

def landing(request):
    return render(request, 'personalai/landing.html', {})

def alert(request):
    return render(request, 'personalai/alert.html', {})

def alert_1(request):
    return render(request, 'personalai/alert_1.html', {})

def alert_2(request):
    return render(request, 'personalai/alert_2.html', {})

def alert_3(request):
    return render(request, 'personalai/alert_3.html', {})

def analytics_1(request):
    return render(request, 'personalai/analytics_1.html', {})

def bestSeller(request):
    return render(request, 'personalai/bestSeller.html', {})

def blank(request):
    return render(request, 'personalai/blank.html', {})

def buttons(request):
    return render(request, 'personalai/buttons.html', {})

def congrats(request):
    return render(request, 'personalai/congrats.html', {})

def email_body(request):
    return render(request, 'personalai/email_body.html', {})

def email_links(request):
    return render(request, 'personalai/email_links.html', {})

def end(request):
    return render(request, 'personalai/end.html', {})

def generalReport(request):
    return render(request, 'personalai/generalReport.html', {})

def head(request):
    return render(request, 'personalai/head.html', {})

def heading_1(request):
    return render(request, 'personalai/heading_1.html', {})

def index(request):
    return render(request, 'personalai/index.html', {})

def introduce_1(request):
    return render(request, 'personalai/index-1.html', {})

def navbar(request):
    return render(request, 'personalai/navbar.html', {})

def numbers(request):
    return render(request, 'personalai/numbers.html', {})

def quickinfo(request):
    return render(request, 'personalai/quickinfo.html', {})

def recent_order(request):
    return render(request, 'personalai/recent_order.html', {})

def salesOverview(request):
    return render(request, 'personalai/salesOverview.html', {})

def sidebar(request):
    return render(request, 'personalai/sidebar.html', {})

def start(request):
    return render(request, 'personalai/start.html', {})

def status(request):
    return render(request, 'personalai/status.html', {})

def summary(request):
    return render(request, 'personalai/summary.html', {})

def typography(request):
    return render(request, 'personalai/typography.html', {})