global choise

def set_lang(in_lang):
    global choise
    choise = in_lang


def curr_lang():
    global choise
    if choise == 1:
        return 1
    elif choise == 2:
        return 0
