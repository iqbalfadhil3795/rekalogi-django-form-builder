from __future__ import unicode_literals

try:
    from django.urls import re_path, include
except ImportError:
    # For Django 1.8 compatibility
    from django.conf.urls import url as re_path, include
from django.contrib import admin
from django.shortcuts import render

from forms_builder.forms.models import Form
from forms_builder.forms import urls as form_urls
#For get change admin site title 
from django.utils.translation import ugettext_lazy as _

admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^forms/', include(form_urls)),
    re_path(r'^$', lambda request: render(request, "index.html",
                                      {"forms": Form.objects.all()})),
]

# Change admin site title
admin.site.site_header = _("Rekalogi Form")
admin.site.site_title = _("Rekalogi Form")