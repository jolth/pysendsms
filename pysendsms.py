#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import threading
from string import Template
import queue
import gammu


# Configure Arguments:
aparser = argparse.ArgumentParser(prog='pysendsms', description='send SMS\
        message from csv file or string using one template.')
group = aparser.add_mutually_exclusive_group()
group.add_argument('-f', '--file',  help='file CSV to reading')
group.add_argument('-m', '--message', help='message to send')
group.add_argument('-t', '--template', help='template for the message. i.e:\
        \'Mr. [$name|${name}] like this\'')
aparser.add_argument('-n', '--number', help='number to sms send')
aparser.add_argument('-i', '--identifiers', help='identifiers that is using\
        into templates')
args = aparser.parse_args()


class SendSMS(threading.Thread):
    def __init__(self):
        pass



if __name__ == '__main__': 
    fifo = queue.Queue()
    
    print(args) #debug Arg

    #print(args.template)
    t = args.template
    if t:
        t = Template(t)
        print(t.substitute())
    else:
        print(t or '')

    #t = Template(args.template) or None
    #if t:
    #    print(t.substitute(name='jorge'))
    #else:
    #    print(t)

