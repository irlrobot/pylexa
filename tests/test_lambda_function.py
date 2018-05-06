#!/usr/bin/env python
import sys
sys.path.insert(0, 'src/')
import pytest
from src.lambda_function import (
    lambda_handler,
    launch_request,
    intent_request,
    end_session_request
)
import request_examples
import response_examples

####################
#lambda_handler
####################
def test_launch_request_in_lambda_handler():
    event = request_examples.launch_request()
    assert lambda_handler(event, 'blah') == 'placeholder'

def test_intent_request_in_lambda_handler():
    event = request_examples.intent_request()
    intent = event['request']['intent']
    assert lambda_handler(event, 'blah') == intent

def test_session_ended_request_in_lambda_handler():
    event = request_examples.session_ended_request()
    response = response_examples.session_ended()
    assert lambda_handler(event, 'blah') == response

def test_lambda_handler_with_keyerror():
    with pytest.raises(KeyError):
        lambda_handler({}, '')

####################
#launch_request
####################
def test_launch_request():
    assert launch_request('blah', 'blah') == 'placeholder'

####################
#intent_request
####################
def test_intent_request():
    event = request_examples.intent_request()
    request = event['request']
    session = event['session']
    intent = event['request']['intent']
    assert intent_request(request, session) == intent

####################
#end_session_request
####################
def test_end_session_request():
    event = request_examples.session_ended_request()
    request = event['request']
    session = event['session']
    response = response_examples.session_ended()
    assert end_session_request(request, session) == response
