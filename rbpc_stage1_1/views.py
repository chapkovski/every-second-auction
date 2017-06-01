from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import django
from django import forms

class Game1(Page):
    def is_displayed(self):
        return self.round_number == 1


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {
            'amount_other_players':
                len(self.group.get_players()) - 1
        }


class Contribute(Page):
    form_model = models.Player
    form_fields = ['contribution']

    def contribution_choices(self):
        # for RPBC_stage1_2 the next line will be:
        # return [0, self.player.participant.vars['counterbalancing'][1]]
        # for RPBC_stage1_3 the next line will be:
        # return [0, self.player.participant.vars['counterbalancing'][2]]
        maxchoice = self.player.participant.vars['counterbalancing'][0]
        choices=[(0,'I am a greedy bastard'),
        (maxchoice, 'I am the most generous guy ever. I will give you {}'.format(maxchoice))]
        return choices


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        return {
            'other_players': self.group.get_players()
        }


class PartnerChoiceForm(forms.Form):
    def __init__(self, choices, *args, **kwargs):
        super(PartnerChoiceForm, self).__init__(*args, **kwargs)
        self.fields['partnerchoice'] = django.forms.CharField(widget=django.forms.RadioSelect(choices=choices),
                                                              label='Which player would you like to play with in Stage 2?')


class FinalPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = models.Player
    form_fields = ['partnerchoice']

    def vars_for_template(self):
        others = self.player.get_others_in_group()
        # we need to show to Player 1 the choice of Player 2 and Player 3, and so on
        choices = [(p.id_in_group, "Player {}".format(p.id_in_group)) for p in others]
        partnerchoiceform = PartnerChoiceForm(tuple(choices))
        return {'myform': partnerchoiceform, }


class WP(WaitPage):
    def after_all_players_arrive(self):
        if self.subsession.round_number == Constants.num_rounds:
            for p in self.group.get_players():
                p.participant.vars['loser'] = not \
                    p.group.get_player_by_id(p.partnerchoice).partnerchoice == p.id_in_group


page_sequence = [
    # Game1,
    # Introduction,
    Contribute,
    ResultsWaitPage,
    # Results,
    # FinalPage,
    # WP
]
