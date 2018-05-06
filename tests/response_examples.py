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

def speech_end_session():
    '''example speech response with ending a session'''
    return {
        "version": "1.0",
        "response": {
            "shouldEndSession": True,
            "outputSpeech": {
                "type": "PlainText",
                "text": 'blah'
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": 'blorp'
                }
            }
        }
    }

def speech_with_card_end_session():
    '''example speech response with card with ending a session'''
    return {
        "version": "1.0",
        "response": {
            "shouldEndSession": True,
            "outputSpeech": {
                "type": "PlainText",
                "text": 'blah'
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": 'blorp'
                }
            },
            "card": {
                "type": "Standard",
                "title": 'card_title',
                "text": 'card_text',
                "image": {
                    "smallImageUrl": 'card_img_sm',
                    "largeImageUrl": 'card_img_lg'
                }
            }
        }
    }

def play_audio_example():
    '''example for sending play audio directive'''
    return {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "directives": [
                {
                    "type": "AudioPlayer.Play",
                    "playBehavior": 'behavior',
                    "audioItem": {
                        "stream": {
                            "token": "doesntreallymatter",
                            "url": 'stream',
                            "offsetInMilliseconds": 0
                        }
                    }
                }
            ],
            "shouldEndSession": True
        }
    }

def stop_audio_example():
    '''example for sending stop audio directive'''
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
