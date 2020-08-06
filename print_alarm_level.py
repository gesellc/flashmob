def print_alarm_level(level):
    if level == 'red':
        response = 'Your dedicated fire person says LOUDLY: "FIRE!"'
    elif level == 'green':
        response = 'Your dedicated fire person says: "All good, nothing to worry about. :)"'
    else:
        response = 'Your dedicated fire person says: "Hmm... do you smell anything?"'
    print(response)