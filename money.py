import random
class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_slepp(self):
        print("I will slepp")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed exetrnally...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "Life"
        print(f"{day:=^50}")
        if live_cube == 1:

        live_cube = random.randint(1, 3)
            self.to_study()
            self.to_slepp()

        elif live_cube == 2:
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()

def money(self):
    if self.progress < -0.5:
        print("Cast out...")
        self.alive = False
    elif self.gladness > 2: #if the student is satisfied, he can buy something for himself in the store
        print("Need to buy something")
        self.alive = False
    elif self.progress > 5: #if a student has earned money somewhere, he can save it for a car
        print("Save money for a car")
        self.alive = False

nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)