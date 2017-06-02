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
from twisted.internet import reactor


author = 'Filipp Chapkovski, UZH'

doc = """
Your app description
"""


from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver



def group_model_exists():
    return 'sandbox1_group' in connection.introspection.table_names()


    # for p in players:
    #     print(p.participant.code)

class Constants(BaseConstants):
    name_in_url = 'sandbox1'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        print('#####', l.__dict__)

        # if not 'background_starts' in self.session.vars:
        #     print('ADDING TASK>>>>>>>>')
        #     self.session.vars['background_starts'] = True

        ...

class Player(BasePlayer):
    auction_winner = models.BooleanField(initial=False)


class Group(BaseGroup):
    price = models.IntegerField(initial=0)
    activated = models.BooleanField()

@receiver(post_save, sender=Group)
def group_handler(sender, **kwargs):
    curgroup = kwargs['instance']





def runEverySecond():

    if group_model_exists():
        activated_groups = Group.objects.filter(activated=True)
        for g in activated_groups:
            g.price += 1
            g.save()
            channels.Group(
                'groupid{}'.format(g.pk)
            ).send(
                {'text': json.dumps(
                    {'price': g.price})}
            )

l = task.LoopingCall(runEverySecond)
if not l.running:
    l.start(1.0) # call every second
