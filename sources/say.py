from .error import say_error

def use(cmd):
    text = cmd[4:]

    if text == "":
        say_error()
    else:
        print(text)