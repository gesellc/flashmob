import requests
import yaml


def detect_fire(picture_url):
    api_response = call_api(picture_url)
    confidence_of_tag_detection = get_tag_confidence(api_response, fire_tag)
    return confidence_of_tag_detection


def call_api(image_url):
    # read credentials from file
    with open(r'config.yml') as file:
        config = yaml.load(file)
    print(config)

    api_key = config['k']
    api_secret = config['s']

    response = requests.get(
        'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
        auth=(api_key, api_secret))

    return response.json()


def get_tag_confidence(api_response, tag):
    #iterate over all available tags in api_response
    #hold current confidence and tag
    #return confidence for specified tag
    print (api_response['result']['tags'][0])
    for tag_entry in api_response['result']['tags']:
        confidence = tag_entry['confidence']
        confidence_tag = tag_entry['tag']['en']
        if confidence_tag == tag:
            return confidence
    return 0