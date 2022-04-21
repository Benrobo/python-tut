from time import sleep



def CountDown(func):
    
    def counter(*args, **kwargs):
        sleep(1)
        return func(*args, **kwargs)
    return counter