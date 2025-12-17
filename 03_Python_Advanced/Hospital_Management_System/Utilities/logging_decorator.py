import os
from datetime import datetime, date

dir_path = os.path.dirname(os.path.abspath(__file__))
logging_file = os.path.join(dir_path, "logging.txt")


def logging_decorator(func):
    def wrapper (*args, **kwargs):
        with open(logging_file, 'a') as f:
            func(*args, **kwargs)
            f.write(f"{datetime.now()}---{func.__name__}---")
    return wrapper

def add():
    print(5+6)
