#!/usr/bin/env python
"""
Skill Name
v1.0.0
github.com/irlrobot
"""
from __future__ import print_function
import json
import responses

def handler(event, context):
    '''
    main function for Lambda
    '''
    print('==============lambda handler started...')
    print(json.dumps(event))

    try:
        request_type = event['request']['type']
    except KeyError:
        request_type = ''

    try:
        intent_name = event['request']['intent']['name']
    except KeyError:
        intent_name = ''

    if request_type == 'LaunchRequest':
        print ('==============LaunchRequest fired...')
    else:
        trigger_intent(intent_name)

def trigger_intent(intent_name):
    '''
    check if intent is
    '''
    print ('==============' + intent_name + ' fired...')
    return eval(intent_name)()
