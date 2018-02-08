from django.db import models as djmodels
from otree.api import models
from random import randint
author = 'Philip Chapkovski'

doc = """
Extention to deal with phone records
"""

from otree.models import Participant, Session


from django.db.models.signals import post_save
from django.dispatch import receiver



# Models for phone identification
class LinkedSession(djmodels.Model):
    session = djmodels.OneToOneField(to=Session, on_delete=djmodels.CASCADE)


class PhoneRecord(djmodels.Model):
    phone_id = models.IntegerField(doc='to store the id')
    # 'link to the session'
    linked_session = djmodels.ForeignKey(to=LinkedSession, on_delete=djmodels.CASCADE, related_name='phonerecords' )
    # 'link to the participant and his correspoinding url'
    participant = djmodels.ForeignKey(to=Participant, on_delete=djmodels.CASCADE,)
    taken = models.BooleanField(default=False, doc='to check whether the record was already used')
    def get_absolute_url(self):
        return self.participant._url_i_should_be_on()

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

@receiver(post_save, sender=LinkedSession)
def create_linked_session(sender, instance, created, **kwargs):
    if created:
        objs = [
            PhoneRecord(
                linked_session=instance,
                participant=p,
                phone_id=random_with_N_digits(10),
            )
            for p in instance.session.get_participants()
        ]
        obj = PhoneRecord.objects.bulk_create(objs)


