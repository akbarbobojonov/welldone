from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from apps.site.views import *

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^about/', About.as_view(), name='about'),
    url(r'^signup/', Signup.as_view(), name='signup'),
    
    url(r'^login/$', auth_views.login, {'template_name': 'site/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'site/registration/logged_out.html'}, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, {
        'template_name': 'site/registration/password_reset_form.html',
        'email_template_name': 'site/registration/password_reset_email.html',
    }, name='password_reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'template_name': 'site/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'site/registration/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'site/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password_reset_complete/$', auth_views.password_reset_complete, {'template_name': 'site/registration/password_reset_complete.html'}, name='password_reset_complete'),
    
    url('^', include('django.contrib.auth.urls')),
]
