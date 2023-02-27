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