from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mails/$', views.handle_mails),
    url(r'^save/$', views.save_obj),
]
