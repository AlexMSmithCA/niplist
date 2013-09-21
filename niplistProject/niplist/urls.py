from django.conf.urls import patterns, include, url

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
)
