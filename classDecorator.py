def add_say_goodbye(cls): # class decorator
    def say_goodbye(self):
        print(f"Goodbye {self.name}")
    cls.say_goodbye = say_goodbye
    return cls

@add_say_goodbye
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello {self.name}")

p = Person("John")
p.say_hello()
p.say_goodbye()