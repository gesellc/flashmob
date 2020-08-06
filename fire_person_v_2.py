from alarm_level_classification_test import get_alarm_level
from detect_fire import detect_fire
from detect_fire_use_case_test import detect_fire_use_case


def get_image_url_use_case():
    print('Please enter image url:')
    return input()


image_url = get_image_url_use_case()

alarm_level = detect_fire_use_case(image_url)


def print_alarm_level(level):
    if level == 'red':
        response = 'Your dedicated fire person says LOUDLY: "FIRE!"'
    elif level == 'green':
        response = 'Your dedicated fire person says: "All good, nothing to worry about. :)"'
    else:
        response = 'Your dedicated fire person says: "Hmm... do you smell anything?"'
    print(response)


print_alarm_level(alarm_level)


