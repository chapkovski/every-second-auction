#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from channels import Group
import json


def ws_connect(message, group_pk):
    print('somebody connected from group:::', group_pk)
    Group('groupid{}'.format(group_pk)).add(message.reply_channel)


def ws_message(message):
    print('MESSAGE RECEIVED!')


def ws_disconnect(message, group_pk):
    print('somebody disconnected...')
    Group('groupid{}'.format(group_pk)).discard(
        message.reply_channel)
