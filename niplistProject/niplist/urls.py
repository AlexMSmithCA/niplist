from django.conf.urls import patterns, include, url

from niplist.facebook import facebook_view

# Generates the routes for the Controller.
# Typical use is a regular expression for a URL pattern, and then the
# action to call to process requests for that URL pattern.
urlpatterns = patterns("",
    url(r"^$", "django.contrib.auth.views.login", {"template_name":"niplist/landing.html"}),
    
    # Authentication routes
    url(r"^login$", "django.contrib.auth.views.login", {"template_name":"niplist/landing.html"}),
    url(r"^logout$", "django.contrib.auth.views.logout_then_login"),
    url(r"^reset-password$", "niplist.views.passwordReset"),
    url(r"^register$", "niplist.views.register"),
    
    # Webapp routes
    url(r"^home$", "niplist.views.home"),
    # Middlewear routes
    url(r'^fb/', facebook_view, name='fb_app'),
    #url(r'^close_login_popup/$', close_login_popup, name='login_popup_close'),
    url(r'', include('social_auth.urls')),
    url(r"^profile$", "niplist.views.profile"),
)
