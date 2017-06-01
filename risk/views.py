from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decisions(Page):
    form_model = models.Player
    form_fields = ['gamble_{}'.format(i) for i in range(1, 11)]

    def vars_for_template(self):
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
