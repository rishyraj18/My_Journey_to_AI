import time

def log_decorator(func):
    def wrapper(*args):
        print(f"Performing : {func.__name__}")
        return func(*args)
    return wrapper