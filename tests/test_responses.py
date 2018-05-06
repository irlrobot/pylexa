import sys
sys.path.insert(0, 'src/')
from src.responses import (
    speech,
    speech_with_card,
    play_audio,
    stop_audio
)
from response_examples import (
    speech_end_session,
    speech_with_card_end_session,
    play_audio_example,
    stop_audio_example
)

####################
#speech
####################
def test_speech():
    assert speech('blah', True, 'blorp') == speech_end_session()

####################
#speech_with_card
####################
def test_speech_with_card():
    assert speech_with_card(
        'blah',
        True,
        'blorp',
        'card_title',
        'card_text',
        'card_img_sm',
        'card_img_lg'
    ) == speech_with_card_end_session()

####################
#play_audio
####################
def test_play_audio():
    assert play_audio('behavior', 'stream') == play_audio_example()

####################
#stop_audio
####################
def test_stop_audio():
    assert stop_audio() == stop_audio_example()
