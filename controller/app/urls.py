from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^send/$', views.send_mails),
    url(r'^save/$', views.save_into_db),
]
