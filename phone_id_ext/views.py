from . import models
import vanilla
from .forms import EmailLookupForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, reverse_lazy


class CreateLinkedSessionView(vanilla.CreateView):
    model = models.LinkedSession
    fields = ['session']
    template_name = 'phone_id_ext/LinkedSessionCreate.html'
    success_url = reverse_lazy('linked_sessions_list')


# to delete linked session
class DeleteLinkedSessionView(vanilla.DeleteView):
    ...


# view to show linked session
class ListLinkedSessionsView(vanilla.ListView):
    template_name = 'phone_id_ext/LinkedSessionList.html'
    url_name = 'linked_sessions_list'
    url_pattern = r'^linked_sessions/$'
    display_name = 'Linked sessions management for Phone surveys'
    model = models.LinkedSession

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        # all_sessions = Session.objects.all()
        # return render(request, self.template_name, {'sessions': all_sessions})


class ListPhoneRecordsView(vanilla.ListView):
    ...
