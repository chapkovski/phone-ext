from django.db import models as djmodels
from otree.api import models

author = 'Philip Chapkovski'

doc = """
Extention to deal with phone records
"""

from otree.models import Participant, Session


# Models for phone identification
class LinkedSession(djmodels.Model):
    session = djmodels.OneToOneField(to=Session, on_delete=models.CASCADE)


class PhoneRecord(djmodels.Model):
    phone_id = models.IntegerField(doc='to store the id')
    # 'link to the session'
    linked_session = djmodels.ForeignKey(to=LinkedSession, on_delete=models.CASCADE, )
    # 'link to the participant and his correspoinding url'
    participant = djmodels.ForeignKey(to=Participant, on_delete=models.CASCADE,)
    taken = models.BooleanField(default=False, doc='to check whether the record was already used')


# class AddedSession(djmodels.Model):
#     session = djmodels.OneToOneField(to=Session)
#
#     def __str__(self):
#         return 'Added session {}'.format(self.session.code)

#
# class ParticipantEmailLookup(models.Model):
#     email = djmodels.EmailField(blank=True, null=True)
#     participant = models.OneToOneField(to=Participant)
#
#     def __str__(self):
#         participant_url = self.participant._url_i_should_be_on()
#         return 'PEL: {}, {}'.format(self.email, participant_url)
#
#     def get_absolute_url(self):
#         return self.participant._url_i_should_be_on()
