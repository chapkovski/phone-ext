
from . import models
import vanilla
from .forms import EmailLookupForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse


class EmailLookupView(vanilla.FormView):
    form_class = EmailLookupForm
    template_name = 'phone_id_ext/email_lookup.html'
    # participant_code = None
    email = None

    def form_valid(self, form):
        self.email = form.cleaned_data['email']
        try:
            PEL = models.ParticipantEmailLookup.objects.get(email=self.email)
        except ObjectDoesNotExist:
            PEL= models.ParticipantEmailLookup.objects.filter(email__isnull=True).first()
            if PEL is None:
                self.success_url = reverse('no_slots')
                return super().form_valid(form)
            else:
                PEL.email = self.email
                PEL.save()


        self.success_url =PEL.get_absolute_url()

        return super().form_valid(form)



