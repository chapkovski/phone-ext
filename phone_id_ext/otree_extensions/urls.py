from django.conf.urls import url, include
from phone_id_ext import views as v

urlpatterns = [url(r'^linkedsession/(?P<lsession>[a-zA-Z0-9_-]+)/delete/$', v.DeleteLinkedSessionView.as_view(),
                   name='delete_linked_session'),
               url(r'^linkedsession/create/$', v.CreateLinkedSessionView.as_view(),
                   name='create_linked_session'),
               url(r'^linkedsession/(?P<lsession>[a-zA-Z0-9_-]+)/phonerecords/$',
                   v.ListPhoneRecordsView.as_view(), name='list_phone_records'),
               ]
