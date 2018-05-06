#!/usr/bin/env python
"""
Example JSON responses to be used for tests
"""

def session_ended():
    '''example session ended response'''
    return {
        "version": "1.0",
        "response": {
            "shouldEndSession": True,
            "outputSpeech": {
                "type": "PlainText",
                "text": "Goodbye"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": str("")
                }
            }
        }
    }
