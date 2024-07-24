import time
def log_time(func):
    def wrapper_function(*args, **kwargs):
        start_timestamp = time.time()
        result = func(*args, **kwargs)
        end_timestamp = time.time()
        execution_duration = end_timestamp - start_timestamp
        print("Start time:", start_timestamp)
        print(f"Execution time of {func.__name__}: {execution_duration:.4f} seconds")
        print("End time:", end_timestamp)
        return result
    return wrapper_function

@log_time
def follow(): 
    print("FOLLOW THE RULES!")

@log_time
def obey(): 
    print("WEAR YOUR HELMETS!")

follow()
obey()

'''
Decorator are basically used to modify the behaviour and function or the method.
Here I have implemented an example of decorator where we have defined a function called log_time which
accepts function's object func. another decorator named wrapper_function which accepts the args and kwargs as 
function parameters.
The *args *args allows you to do is take variable, the **kwargs allows you to take dictionary argument which
will need key-value.
'''