import random
class Student:
    def __init__(self, name, ):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 1000
        self.days = random.randint(1, 366)

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3
        self.money -= 200


    def to_work(self):
        print("I am working")
        work_cube = random.randint(0, 8)
        if work_cube == 0:
            self.money += 0
        elif work_cube == 1:
            self.money += 10
        elif work_cube == 2:
            self.money += 20
        elif work_cube == 3:
            self.money += 30
        elif work_cube == 4:
            self.money += 40
        elif work_cube == 5:
            self.money += 50
        elif work_cube == 6:
            self.money += 60
        elif work_cube == 7:
            self.money += 70
        elif work_cube == 8:
            self.money += 80


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
        self.money -= 400

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 400


    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.days > 365:
            print("I die")
            self.alive = False


    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day " + str(self.days) + " of " + self.name + " life"
        if self.alive == True:
            print(f"{day:=^50}")
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
                self.end_of_day()
                self.is_alive()
            elif live_cube == 4:
                self.to_work()
        elif self.alive == False:
            print("on 366 day" + self.name + "die")

    def __str__(self):
        return f"My name is {self.name}"

anton = Student("Anton")

print(anton)
anton.live("")
anton.is_alive()