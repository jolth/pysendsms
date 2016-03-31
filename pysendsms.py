#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pysendsms.py -t 'Sr. $name, your number account is active' -i {'name':'jorge'}
"""
import argparse
import threading
from string import Template
import gammu
import json


# Configure Arguments:
aparser = argparse.ArgumentParser(prog='pysendsms', description='send SMS\
        message from csv file or string using one template.')
group = aparser.add_mutually_exclusive_group()
group.add_argument('-f', '--file',  help='file CSV to reading')
group.add_argument('-m', '--message', help='message to send')
group.add_argument('-t', '--template', help='template for the message. i.e:\
        \"Sr. [$name|${name}], your number account is not active\"')
aparser.add_argument('-n', '--number', help='number to sms send')
aparser.add_argument('-i', '--identifiers', help='identifiers that is using\
        into templates. i.e: {"name":"jorge",...}')
args = aparser.parse_args()


class SendSMS(threading.Thread):
    """class using for create and sending to message"""
    def __init__(self, fifo):
        self.fifo = fifo
        threading.Thread.__init__(self)

    def run(self):
        pass


def identifiers(i: str) -> dict:
    """return one dictionary with all identifiers"""
    i = json.loads(i.replace('\'', '\"'))
    return i


class Arguments(object):
    """the Argument class is a container of methods for the arguments."""

    def __init__(self, args: list):
        self._args = args
        print(self._args) #debug
        self.toCallArg()

    def toCallArg(self):
        """parser from arguments"""
        for key, value in dict(self._args._get_kwargs()).items():
            print(hasattr(self, key), value) #debug
            if value and hasattr(self, key):
                print('KEY:', key) #debug
                print(callable(getattr(self, key))) #debug
                print(getattr(self, key)()) #debug
                break

    def file(self):
        return 'FILE'

    def template(self):
        return 'TEMPLATE 1'

    def identifiers(self):
        return 'IDENTIFIERS'

    def message(self):
        return 'MESSAGE'

    def number(self):
        return 'NUMBER'


if __name__ == '__main__': 
 
    arg =  Arguments(args)
