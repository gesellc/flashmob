import pytest


def test_example():
    assert "This" == "This"

import requests
import yaml

def test_request():
    with open(r'config.yml') as file:
        yaml.load(file)

    api_key = '<replace-with-your-api-key>'
    api_secret = '<replace-with-your-api-secret>'
    image_url = 'https://docs.imagga.com/static/images/docs/sample/japan-605234_1280.jpg'

    response = requests.get(
        'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
        auth=(api_key, api_secret))

    print(response.json())
