from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from  django.template import Context,Template


class Decisions(Page):
    form_model = models.Player
    form_fields = ['gamble_{}'.format(i) for i in range(1, 11)]


# class DecisionsA(Page):
#     pass
# class DecisionsB(Page):
#     pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Decisions,
    # DecisionsA,
    # DecisionsB
]
