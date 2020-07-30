from alarm_level_classification_test import get_alarm_level
from detect_fire import detect_fire

# fire  = 'https://images.unsplash.com/photo-1507019658682-2924f9dbd499?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80'

# no_fire = 'https://docs.imagga.com/static/images/docs/sample/japan-605234_1280.jpg'

# maybe_fire = 'https://images.unsplash.com/photo-1574159087201-e2147a95910d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1191&q=80'

print('Please enter image url:')
image_url = input()
#print(image_url)

confidence = detect_fire(image_url)
alarm_level = get_alarm_level(confidence)

if alarm_level == 'red':
    response = 'Your dedicated fire person says LOUDLY: "FIRE!"'
elif alarm_level == 'green':
    response = 'Your dedicated fire person says: "All good, nothing to worry about. :)"'
else:
    response = 'Your dedicated fire person says: "Hmm... do you smell anything?"'

print(response)


