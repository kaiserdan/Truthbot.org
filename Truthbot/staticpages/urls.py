from django.conf.urls import url

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="staticpages/index.html"), name='homepage'),
    url(r'^about/$', TemplateView.as_view(template_name="staticpages/about.html"), name='about'),
    url(r'^donate/$', TemplateView.as_view(template_name="staticpages/donate.html"), name='donate'),
    url(r'^reddit/$', TemplateView.as_view(template_name="staticpages/reddit.html"), name='reddit'),
    url(r'^loaderio-161269a99b26b52e85511a4334c564af/$', TemplateView.as_view(template_name="staticpages/loader.html")),
]
