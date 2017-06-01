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
    ...


for i in range(1,11):
    Player.add_to_class("gamble_{}".format(i),
                        models.BooleanField())
