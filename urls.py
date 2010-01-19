from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^attachments/', include('attachments.urls')),
    (r'^article/', include('article.urls')),
    (r'^profile/', include('profile.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Password recovery
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', {'template_name':'password/password_reset_form.html', 'email_template_name':'email/password_reset_email.txt', 'password_reset_form':PasswordResetForm}, name="password_reset"),
    (r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name':'password/password_reset_done.html'}),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name':'password/password_reset_confirm.html'}),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name':'password/password_reset_complete.html'}),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'base.html'}),
    #url(r'^$', 'direct_to_template', {'template': 'construct.html'}, name='under_construction'),
    url(r'^about_me/$', 'direct_to_template', {'template': 'about_me.html', 'extra_context':{'current': 'about'}}, name='about_me'),
    )   

