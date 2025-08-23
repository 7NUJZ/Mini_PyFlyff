import threading


def multithreading(function):
    t = threading.Thread(target=function)

    t.setDaemon(True)

    t.start()


def validate_input_timers(char):
    if char.isdigit() or char == "," or char == ".":

        return True

    else:

        return False


def validate_input_keys(char):
    if char.isalnum() or char == ",":

        return True

    else:

        return False


def validate_input_buffer_key(char):
    # Allow alphanumeric characters and empty string (for deletion)
    if char.isalnum() or char == "":

        return True

    else:

        return False


def validate_input_buffer_timer(char):
    # Allow digits and empty string (for deletion)
    if char.isdigit() or char == "":

        return True

    else:

        return False
