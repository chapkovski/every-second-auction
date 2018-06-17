from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
# from background_task import background
# from background_task.models import Task
import atexit
import subprocess
from django.db import transaction, models as dmodels
import channels
import json
from django.db import connection

from twisted.internet import task



author = 'Filipp Chapkovski, chapkovski@gmail.com'

doc = """
Your app description
"""


from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver



def group_model_exists():
    return 'volunteer_group' in connection.introspection.table_names()


    # for p in players:
    #     print(p.participant.code)

class Constants(BaseConstants):
    name_in_url = 'volunteer'
    players_per_group = 3
    num_rounds = 1
    endowment = 50
    instruction_template = 'volunteer/Instructions.html'

class Subsession(BaseSubsession):
    def before_session_starts(self):
        ...

class Player(BasePlayer):
    auction_winner = models.BooleanField(initial=False)
    def set_payoff(self):
        self.payoff = (Constants.endowment - self.group.price * self.auction_winner) * (not self.group.timeout)

class Group(BaseGroup):
    price = models.IntegerField(initial=0)
    activated = models.BooleanField()
    timeout = models.BooleanField(initial = False)




def runEverySecond():
    print('checking if there are active groups...')
    if group_model_exists():
        activated_groups = Group.objects.filter(activated=True)
        for g in activated_groups:
            if g.price < Constants.endowment:
                g.price += 1
                g.save()
                channels.Group(
                    'groupid{}'.format(g.pk)
                ).send(
                    {'text': json.dumps(
                        {'price': g.price})}
                )
            else:
                g.timeout = True
                g.save()
                advance_participants([p.participant for p in g.get_players()])


l = task.LoopingCall(runEverySecond)
if not l.running:
    l.start(1.0)
