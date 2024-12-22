def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

def say_whee(name):
    print(f"Whee! {name}")

say_whee = my_decorator(say_whee)
say_whee("John")