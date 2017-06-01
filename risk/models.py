from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from  django.template import Context,Template


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'risk_aversion'
    players_per_group = None
    num_rounds = 1

    risk_takers_payoff_1 = c(10)
    risk_takers_payoff_2 = c(0.25)
    risk_averse_payoff_1 = c(5)
    risk_averse_payoff_2 = c(4)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gamble_1 = models.BooleanField()
    gamble_2 = models.BooleanField()
    gamble_3 = models.BooleanField()
    gamble_4 = models.BooleanField()
    gamble_5 = models.BooleanField()
    gamble_6 = models.BooleanField()
    gamble_7 = models.BooleanField()
    gamble_8 = models.BooleanField()
    gamble_9 = models.BooleanField()
    gamble_10 = models.BooleanField()

