#!/usr/bin/env python
import os
import sys

# from twisted.internet import protocol, reactor
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    # print('starting server....')
    # reactor.run()
    from otree.management.cli import execute_from_command_line
    execute_from_command_line(sys.argv, script_file=__file__)
