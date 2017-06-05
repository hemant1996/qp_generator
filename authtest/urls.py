# -*- coding: utf-8 -*-
#!python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
from log.forms import LoginForm
from django.contrib import admin

# Text to put at the end of each page's <title>.
admin.site.site_title = 'QUESTIONATOR'

# Text to put in each page's <h1>.
admin.site.site_header = 'QUESTIONATOR ADMIN'

# Text to put at the top of the admin index page.
admin.site.index_title = 'QUESTIONATOR ADMIN'
urlpatterns = [
url(r'^admin/', include(admin.site.urls)),
url(r'', include('log.urls')),
url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
url(r'^logout/$', views.logout, {'next_page': '/login'}),
url(r'^sub/$', 'log.views.download',name='download'),
url(r'^mcq/$', 'log.views.downloadmcq',name='mcq'),]