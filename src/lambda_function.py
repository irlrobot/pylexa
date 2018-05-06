#!/usr/bin/env python
"""
Skill Name
v2.0.0
github.com/irlrobot
"""
from __future__ import print_function
import json
import responses

def lambda_handler(event, _context):
    '''main function for AWS Lambda'''
    print('=====lambda handler started...')
    print(json.dumps(event))

    try:
        if event['request']['type'] == "LaunchRequest":
            return launch_request(event['request'], event['session'])
        if event['request']['type'] == "IntentRequest":
            return intent_request(event['request'], event['session'])
        if event['request']['type'] == "SessionEndedRequest":
            return end_session_request(event['request'], event['session'])
    except KeyError as err:
        print("=====ERROR bad request: " + err)
        raise

def launch_request(request, session):
    '''handles modal launches'''
    print("=====launch request...")

def intent_request(request, session):
    '''route intent'''
    intent = request['intent']
    intent_name = request['intent']['name']
    print("=====intent is: " + intent_name)
    if intent_name == "BLAH":
        print("=====BLAH intent...")
        return blah(intent, session)

def end_session_request(request, session):
    '''handles stop/exit/quit'''
    print("=====end session request...")
    responses.speech("Goodbye", True, "")
