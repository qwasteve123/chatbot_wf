import time

def count_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"Elapsed time for {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

