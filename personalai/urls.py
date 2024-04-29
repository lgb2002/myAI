from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('landing.html', views.landing, name='landing'),
    path('index.html', views.introduce, name='introduce'),
    path('index-1.html', views.introduce_1, name='introduce_1'),
    path('email.html', views.email, name='email'),
    path('1_btns.html', views.btns_1, name='btns_1'),
    path('2_btns.html', views.btns_2, name='btns_2'),
    path('alert.html', views.alert, name='alert'),
    path('alert_1.html', views.alert_1, name='alert_1'),
    path('alert_2.html', views.alert_2, name='alert_2'),
    path('alert_3.html', views.alert_3, name='alert_3'),
    path('analytics-1.html', views.analytics_1, name='analytics_1'),
    path('bestSeller.html', views.bestSeller, name='bestSeller'),
    path('blank.html', views.blank, name='blank'),
    path('buttons.html', views.buttons, name='buttons'),
    path('blank.html', views.blank, name='blank'),
    path('buttons.html', views.buttons, name='buttons'),
    path('congrats.html', views.congrats, name='congrats'),
    path('email-body.html', views.email_body, name='email_body'),
    path('email-links.html', views.email_links, name='email_links'),
    path('end.html', views.end, name='end'),
    path('generalReport.html', views.generalReport, name='generalReport'),
    path('head.html', views.head, name='head'),
    path('heading_1.html', views.heading_1, name='heading_1'),
    path('navbar.html', views.navbar, name='navbar'),
    path('numbers.html', views.numbers, name='numbers'),
    path('quickinfo.html', views.quickinfo, name='quickinfo'),
    path('recent_order.html', views.recent_order, name='recent_order'),
    path('salesOverview.html', views.salesOverview, name='salesOverview'),
    path('sidebar.html', views.sidebar, name='sidebar'),
    path('start.html', views.start, name='start'),
    path('status.html', views.status, name='status'),
    path('summary.html', views.summary, name='summary'),
    path('typography.html', views.typography, name='typography'),
]