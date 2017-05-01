#!/usr/bin/env python
"""
Helper Module for building Alexa responses
"""
from __future__ import print_function
import json

'''
Long Form Audio
'''
def play_audio(behavior, stream):
    '''
    Send AudioPlayer.Play Directive
    '''
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": behavior,
                    "audioItem": {
                        "stream": {
                            "token": "doesntreallymatter",
                            "url": stream,
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }

def stop_audio():
    '''
    Send AudioPlayer.Stop Directive
    '''
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Stop",
                }
            ],
            "shouldEndSession": True
        }
    }

"""
Custom
"""
def speech(tts, end_session):
    '''
    build speech output
    '''
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": tts
            }
        },
        "shouldEndSession": end_session
    }

def speech_with_card(tts, end_session, card_title, card_text, card_img_sm, card_img_lg):
    '''
    build speech output
    '''
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": tts
            },
            "card": {
                "type": "Standard",
                "title": card_title,
                "text": card_text,
                "image": {
                    "smallImageUrl": card_img_sm,
                    "largeImageUrl": card_img_lg
                }
            }
        },
        "shouldEndSession": end_session
    }
