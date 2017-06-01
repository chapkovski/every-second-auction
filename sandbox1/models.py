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


from twisted.internet import task
from twisted.internet import reactor


author = 'Filipp Chapkovski, UZH'

doc = """
Your app description
"""


from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver



def runEverySecond():
    # players = Player.objects.all()
    print('WE ARE RUNNING EVERY SECNOD!!!')
    channels.Group('hellow').send(
            {'text': json.dumps(
                {'price': 123})}
        )
    # for p in players:
    #     print(p.participant.code)

l = task.LoopingCall(runEverySecond)
l.start(1.0) # call every second

class Constants(BaseConstants):
    name_in_url = 'sandbox1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):

        if not 'background_starts' in self.session.vars:
            print('ADDING TASK>>>>>>>>')
            self.session.vars['background_starts'] = True

            ...

class Player(BasePlayer):
    ...


class Group(BaseGroup):
    price = models.IntegerField(initial=0)
    update_price = models.BooleanField()

# @receiver(post_save, sender=Group)
# def my_handler(sender, **kwargs):
#     group_pk = kwargs['instance'].pk
#     channels.Group('hellow').send(
#             {'text': json.dumps(
#                 {'price': 123})}
#         )
#     print('GROUP HAS CHANGED')
#
#
# @transaction.atomic
# @background()
# def change_price():
#     print('we are at background.....')
#     updating_groups = Group.objects.filter(update_price=True)
#     for g in updating_groups:
#         g.price += 1
#         g.save()
#         channels.Group('hellow').send(
#                 {'text': json.dumps(
#                     {'price': g.price})}
#             )

# @transaction.atomic
# @background()
# def change_price():
#     print('we are at background.....')
#     channels.Group('hellow').send(
#             {'text': json.dumps(
#                 {'price': 123})}
#         )



process = subprocess.Popen(['echo', 'asdf'], )
# process = subprocess.Popen(['python', 'manage.py', 'process_tasks'], )
# def cleanup():
#     print('############### cleaning and terminating... $$$$$$$$$$')
    # Task.objects.all().delete()
    # subprocess.run(['killall', 'python', 'manage.py', 'process_tasks'], )
    # process.terminate()

# atexit.register(cleanup)
