from django.db import models

author = 'Your name here'

doc = """
Your app description
"""

from otree.models import Participant, Session


# Models for phone identification
class LinkedSession(models.Model):
    session = models.OneToOneField(to=Session, on_delete=models.CASCADE)

class PhoneRecord(models.Model):
    phone_id = models.IntegerField()
    linked_session=models.ForeignKey(to=LinkedSession)
    participant=models.ForeignKey(to=Participant)

class AddedSession(models.Model):
    session = models.OneToOneField(to=Session)

    def __str__(self):
        return 'Added session {}'.format(self.session.code)


class ParticipantEmailLookup(models.Model):
    email = models.EmailField(blank=True, null=True)
    participant = models.OneToOneField(to=Participant)

    def __str__(self):
        participant_url = self.participant._url_i_should_be_on()
        return 'PEL: {}, {}'.format(self.email, participant_url)

    def get_absolute_url(self):
        return self.participant._url_i_should_be_on()
