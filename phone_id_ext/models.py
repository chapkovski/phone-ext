from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from django.db import models as djmodels

author = 'Your name here'

doc = """
Your app description
"""

from otree.models import Participant, Session


class AddedSession(djmodels.Model):
    session = djmodels.OneToOneField(to=Session)
    def __str__(self):
        return 'Added session {}'.format(self.session.code)


class ParticipantEmailLookup(djmodels.Model):
    email = djmodels.EmailField(blank=True, null=True)
    participant = djmodels.OneToOneField(to=Participant)
    def __str__(self):
        participant_url = self.participant._url_i_should_be_on()
        return 'PEL: {}, {}'.format(self.email, participant_url)

    def get_absolute_url(self):
        return self.participant._url_i_should_be_on()
