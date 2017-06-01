from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decisions(Page):
    form_model = models.Player
    form_fields = ['gamble_{}'.format(i) for i in range(1, 11)]

    def vars_for_template(self):
        # a = Variable('form').resolve(self.context)
        smth = self.get_form()
        fields_to_show=self.form_fields
        leftcol = []
        rightcol = []
        maxlen = len(fields_to_show)+1
        for i, f in enumerate(fields_to_show):
            str1 = ', '.join(str(e) for e in [_ for _ in range(1, i+2)])
            str2 = ', '.join(str(e) for e in [_ for _ in range(i+2, maxlen )])
            leftcol.append(str1)
            rightcol.append(str2)

        return {'abclist':zip(smth,leftcol,rightcol),}
# class DecisionsA(Page):
#     pass
# class DecisionsB(Page):
#     pass


class Detection(Page): #here the decision to detect the TLS is taken
    form_model = models.Player


    # def get_form_fields(self):
    #     others = self.player.get_others_in_group()
    #     fields_to_show = ['detectP{}'.format(p.id_in_group) for p in others if p.isTLC]
    #     return fields_to_show

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
