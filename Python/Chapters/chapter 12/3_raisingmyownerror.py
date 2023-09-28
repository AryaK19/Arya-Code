from ctypes.wintypes import HHOOK


def increment(a):
    try:
        a = int(a) + 1
        return print(a)
        #here i raised my own error inspite the type of error it was
    except:
        raise ValueError("Costum Msg.")
        

increment('')
