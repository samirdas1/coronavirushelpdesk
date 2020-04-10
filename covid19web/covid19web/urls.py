"""covid19web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from covid19app.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', corona_virus_helpdesk),
    url('aboutus.html', aboutus),
    path('helplineno.html', helplineno),
    path('helpus.html', helpus),
    path('login_page.html', login_page),
    path('map.html', map),
    path('map2.html', map2),
    path('states.html', states),
    path('data.html', p_data),
    path('form.html', p_help)

    # url(r'aboutus.html', aboutus),

    #url('help', p_help)

]

urlpatterns += staticfiles_urlpatterns()
