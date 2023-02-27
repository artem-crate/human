class Wow:
    def __wow(self):
        print("Wow")
    def _hello(self):
        print("Hello")

some_obj = Wow()
some_obj._hello()
some_obj._Wow__wow()

class Hello:
    def __init__(self):
        print("Hello!")
class Hello_World(Hello):
        def __init__(self):
            super().__init__()
            print("World!")
hello_world = Hello_World()

class Grandparent:
    def about(self):
        print("I am Grandparent")
    def about_myself(self):
        print("I am Grandparent")
class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")
class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()
nick = Child()

# class Animal:
#     def about(self):
#         print("Meow")
#     def about_myself(self):
#         print("Meow")
# class Dog(Animal):
#     def about_myself(self):
#         print("Woof")
# class Cat(Animal):
#     def __init__(self):
#         super().about()
#         super().about_myself()
# nick = Cat()

class Laptop:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128

class Joystick:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "1.000UAH"
class Tablet(Joystick, Laptop):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)
iphone = Tablet(model ="Last")
iphone.print_info()

