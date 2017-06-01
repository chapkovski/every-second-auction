#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from channels import Group
import json

# def ws_connect(message, group_pk):
#     # print('????GROUP NAME:::: ', 'groupid{}'.format(group_pk))
#     # print('somebody connected from group:::', group_pk)
#     print('FUcK')
#     Group('groupid{}'.format(group_pk)).add(message.reply_channel)
#     print('$$$$$$$$$$$$$$::::', Group('groupid{}'.format(group_pk)).__dict__)
#
#
# def ws_message(message):
#     print('MESSAGE RECEIVED!')
#
#
# def ws_disconnect(message, group_pk):
#     print('somebody disconnected...')
#     Group('groupid{}'.format(group_pk)).discard(
#         message.reply_channel)
# ###########

def ws_connect(message):
    # print('????GROUP NAME:::: ', 'groupid{}'.format(group_pk))
    print('somebody connected from group:::')
    # print('FUcK')
    Group('hellow').add(message.reply_channel)
    # print('$$$$$$$$$$$$$$::::', Group('groupid{}'.format(group_pk)).__dict__)


def ws_message(message):
    print('MESSAGE RECEIVED!')


def ws_disconnect(message):
    print('somebody disconnected...')
    Group('hellow').discard(
        message.reply_channel)
