from contextlib import contextmanager
from time import perf_counter

@contextmanager
def timed(metrics:dict,key:str):
    start=perf_counter()
    try: yield
    finally: metrics[key]=perf_counter()-start
