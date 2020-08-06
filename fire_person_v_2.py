from detect_fire_use_case_test import detect_fire_use_case
from get_image_url_use_case import get_image_url_use_case
from print_alarm_level import print_alarm_level

image_url = get_image_url_use_case()

alarm_level = detect_fire_use_case(image_url)

print_alarm_level(alarm_level)


