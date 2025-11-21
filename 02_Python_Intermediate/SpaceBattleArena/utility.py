import time

def log_decorator(func):
    def wrapper(*args):
        print(f"Performing : {func.__name__}")
        return func(*args)
    return wrapper

def cooldown(seconds):
    last_call = 0
    def cooldown_deorator(func):
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.time()
            if (now - last_call) < seconds:
                print("Please wait for Cooling Down")
            else:
                func(*args, **kwargs)
                last_call = time.time()
        return wrapper
    return cooldown_deorator
