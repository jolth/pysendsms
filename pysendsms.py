#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pysendsms.py.aux -t 'Sr. $name, your number account is active' -i {'name':'jorge'}"
"""
import argparse
import threading
from string import Template
import queue
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

fifo = queue.Queue()

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
        self.args = args
        print(self.args) #debug
        self.toCallArg()

    def toCallArg(self):
        """parser from arguments"""
        for key, value in dict(self.args._get_kwargs()).items():
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


#def arg_parser


if __name__ == '__main__': 
 
    #if args.identifiers is not None:
    #if args.identifiers:
    #    print(identifiers(args.identifiers)) #debug

    arg =  Arguments(args)
    #for key, value in dict(args._get_kwargs()).items():
    #    print(hasattr(arg, key), value) #debug
    #    if value and hasattr(arg, key):
    #        print('KEY:', key) #debug
    #        print(callable(getattr(arg, key))) #debug
    #        print(getattr(arg, key)()) #debug
    #        break

    #print(arg.template())

   #print(args) #debug arg

    #def foo(*a):
    #    print(a)

    #foo(*args)
    #print(dir(args)) #debug
    #for i in args:
     #   print(i)
    #print(args._get_args()) #debug
    #print(args._get_kwargs()) #debug

    
