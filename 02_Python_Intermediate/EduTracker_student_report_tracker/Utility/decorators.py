import time

def validate_input(func):
    def wrapper(value):
        if value:
            return func(value)
        else:
            return "unknown arguments\nExiting"
    return wrapper

def log_action(func):
    def wrapper(*args):
        print(f"Executing funtion: {(func.__name__).title()}")
        func(*args)
        print("Function execution Done")
    return wrapper

def performance_check(func):
    def wrapper(*args):
        st = time.time()
        func(*args)
        et = time.time()
        print(f"Time Taken for executing function {(func.__name__).title()}: {(et-st):.4f}")
    return wrapper