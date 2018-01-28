from django.conf.urls import url, include
from django.views.generic import TemplateView
from phone_id_ext import views as v
import vanilla
from django.contrib.auth.decorators import login_required
urlpatterns = [url(r'^email_lookup/$', v.EmailLookupView.as_view(),
                   name='email_lookup'),
               url(r'^no_slots/$', vanilla.TemplateView.as_view(template_name='phone_id_ext/no_slots.html'),
                   name='no_slots'),
               ]
