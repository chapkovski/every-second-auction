# -*- coding: utf-8 -*-
import logging
import channels
import json
import django.test


from otree import constants_internal
from otree.common_internal import get_admin_secret_code
from otree.db import models
from otree.models.session import Session

client = django.test.Client()

ADMIN_SECRET_CODE = get_admin_secret_code()


def advance_participants(group_members):
    for p in group_members:
        try:
            if p._current_form_page_url:
                resp = client.post(
                    p._current_form_page_url,
                    data={
                        constants_internal.timeout_happened: True,
                        constants_internal.admin_secret_code: ADMIN_SECRET_CODE
                    },
                    follow=True
                )
            else:
                resp = client.get(p._start_url(), follow=True)
        except:
            logging.exception("Failed to advance participant.")
            raise

        assert resp.status_code < 400
        channels.Group(
            'auto-advance-{}'.format(p.code)
        ).send(
            {'text': json.dumps(
                {'auto_advanced': True})}
        )
