import pytest

from alarm_level_classification_test import get_alarm_level
from detect_fire import detect_fire


def detect_fire_use_case(image_url):
    confidence = detect_fire(image_url)
    return get_alarm_level(confidence)

def test_no_fire_detected():
    no_fire_image_url = 'https://docs.imagga.com/static/images/docs/sample/japan-605234_1280.jpg'
    assert detect_fire_use_case(no_fire_image_url) == 'green'

def test_potential_danger_detected():
    maybe_fire_image_url = 'https://images.unsplash.com/photo-1528227436006-bf774de37e4d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80'
    assert detect_fire_use_case(maybe_fire_image_url) == 'yellow'

def test_fire_detected():
    fire_image_url = 'https://images.unsplash.com/photo-1507019658682-2924f9dbd499?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80'
    assert detect_fire_use_case(fire_image_url) == 'red'