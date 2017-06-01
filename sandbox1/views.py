from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import json
import channels


class MyPage(Page):
    form_model = models.Group
    form_fields = ['price']

    def vars_for_template(self):
        self.group.update_price = True
    #     channels.Group(
    #         'group_id-{}'.format(self.group.pk)
    #     ).send(
    #         {'text': json.dumps(
    #             {'price': self.group.price})}
    #     )
    # def before_next_page(self):
    #     self.group.update_price = False
    #     channels.Group('hellow').send(
    #             {'text': json.dumps(
    #                 {'price': self.group.price})}
    #         )

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
