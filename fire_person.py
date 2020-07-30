from alarm_level_classification_test import get_alarm_level
from detect_fire import detect_fire

#image_url = 'https://images.unsplash.com/photo-1507019658682-2924f9dbd499?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80'

image_url = input()
#print(image_url)

confidence = detect_fire(image_url)
alarm_level = get_alarm_level(confidence)

print(alarm_level)