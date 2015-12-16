CODE = ['wink', 'double blink', 'close your eyes', 'jump']

def convert_to_binary(decimal):
    return bin(decimal)[2:]

def process_binary(raw_binary):
    return len(raw_binary) == 5, raw_binary[-4:][::-1]

def convert_to_and_process_binary(decimal):
    return process_binary(convert_to_binary(decimal))

def binary_to_action(processed_binary):
    reverse, binary = processed_binary
    if any(x not in ['0', '1'] for x in binary):
        return []
    actions = [action for action, binary in zip(CODE, binary) if binary == '1']
    return list(reversed(actions)) if reverse else actions

def decimal_to_action(number):
    if number < 0:
        return []
    processed_binary = convert_to_and_process_binary(number)
    return binary_to_action(processed_binary)

def handshake(number):
    if isinstance(number, int):
        return decimal_to_action(number)
    return binary_to_action(process_binary(number))


def code(actions):
    if any(action not in CODE for action in actions):
        return '0'

    reverse = len(actions) > 1 and actions[1] not in CODE[CODE.index(actions[0]):]
    if reverse:
        string = "1"
    else:
        string = ""

    for action in reversed(CODE):
        if action in actions:
            string += '1'
        elif string:
            string += '0'
    return string