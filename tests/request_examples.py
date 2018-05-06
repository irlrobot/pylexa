#!/usr/bin/env python
"""
Example JSON requests to be used for tests
"""

def launch_request():
    '''example launch request
    https://developer.amazon.com/docs/custom-skills/request-types-reference.html#launchrequest-example
    '''
    return {
        "version": "1.0",
        "session": {
            "new": True,
            "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
            "application": {
            "applicationId": "amzn1.echo-sdk-ams.app.000000-d0ed-0000-ad00-000000d00ebe"
            },
            "attributes": {},
            "user": {
            "userId": "amzn1.account.AM3B00000000000000000000000"
            }
        },
        "context": {
            "System": {
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.000000-d0ed-0000-ad00-000000d00ebe"
            },
            "user": {
                "userId": "amzn1.account.AM3B00000000000000000000000"
            },
            "device": {
                "supportedInterfaces": {
                "AudioPlayer": {}
                }
            }
            },
            "AudioPlayer": {
            "offsetInMilliseconds": 0,
            "playerActivity": "IDLE"
            }
        },
        "request": {
            "type": "LaunchRequest",
            "requestId": "amzn1.echo-api.request.0000000-0000-0000-0000-00000000000",
            "timestamp": "2015-05-13T12:34:56Z",
            "locale": "string"
        }
    }

def intent_request():
    '''example intent request
    https://developer.amazon.com/docs/custom-skills/request-types-reference.html#intentrequest-example
    '''
    return {
        "version": "1.0",
        "session": {
            "new": False,
            "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
            "application": {
            "applicationId": "amzn1.echo-sdk-ams.app.000000-d0ed-0000-ad00-000000d00ebe"
            },
            "attributes": {
            "supportedHoroscopePeriods": {
                "daily": True,
                "weekly": False,
                "monthly": False
            }
            },
            "user": {
            "userId": "amzn1.account.AM3B00000000000000000000000"
            }
        },
        "context": {
            "System": {
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.000000-d0ed-0000-ad00-000000d00ebe"
            },
            "user": {
                "userId": "amzn1.account.AM3B00000000000000000000000"
            },
            "device": {
                "supportedInterfaces": {
                "AudioPlayer": {}
                }
            }
            },
            "AudioPlayer": {
            "offsetInMilliseconds": 0,
            "playerActivity": "IDLE"
            }
        },
        "request": {
            "type": "IntentRequest",
            "requestId": " amzn1.echo-api.request.0000000-0000-0000-0000-00000000000",
            "timestamp": "2015-05-13T12:34:56Z",
            "dialogState": "COMPLETED",
            "locale": "string",
            "intent": {
            "name": "BLAH",
            "confirmationStatus": "NONE",
            "slots": {
                "ZodiacSign": {
                "name": "ZodiacSign",
                "value": "virgo",
                "confirmationStatus": "NONE"
                }
            }
            }
        }
    }

def session_ended_request():
    '''example session ended request
    https://developer.amazon.com/docs/custom-skills/request-types-reference.html#sessionendedrequest-example
    '''
    return {
        "version": "1.0",
        "session": {
            "new": False,
            "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
            "application": {
            "applicationId": "amzn1.echo-sdk-ams.app.000000-d0ed-0000-ad00-000000d00ebe"
            },
            "attributes": {
            "supportedHoroscopePeriods": {
                "daily": True,
                "weekly": False,
                "monthly": False
            }
            },
            "user": {
            "userId": "amzn1.account.AM3B00000000000000000000000"
            }
        },
        "context": {
            "System": {
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.000000-d0ed-0000-ad00-000000d00ebe"
            },
            "user": {
                "userId": "amzn1.account.AM3B00000000000000000000000"
            },
            "device": {
                "supportedInterfaces": {
                "AudioPlayer": {}
                }
            }
            },
            "AudioPlayer": {
            "offsetInMilliseconds": 0,
            "playerActivity": "IDLE"
            }
        },
        "request": {
            "type": "SessionEndedRequest",
            "requestId": "amzn1.echo-api.request.0000000-0000-0000-0000-00000000000",
            "timestamp": "2015-05-13T12:34:56Z",
            "reason": "USER_INITIATED",
            "locale": "string"
        }
    }
