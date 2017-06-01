from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools

author = 'Scott'

doc = """
Stage 1 of the RBPC experiment: Game 1
"""


class Constants(BaseConstants):
    name_in_url = 'RBPC_Stage1_1'
    players_per_group = 3
    num_rounds = 2

    endowment = c(100)
    efficiency_factor = 1.5



class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['loser'] = False


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = (self.total_contribution * Constants.efficiency_factor) / Constants.players_per_group
        for p in self.get_players():
            p.payoff = Constants.endowment - (p.contribution) + self.individual_share

class Player(BasePlayer):
    contribution = models.PositiveIntegerField(
        widget=widgets.RadioSelect()
    )
    partnerchoice = models.IntegerField()
