import random


cars = { "BMW" : {"fuel": 100, "speed":130},
        "jiguli": {"fuel": 80, "speed": 90}
}

jobs = { "builder": {"salary": 150, "energy": 100},
         "taxist": {"salary": 70, "energy": 250},
}


chill = { "home": {"money": 200, "energy": 300},
          "beach": {"money": 300, "energy": 200}

}

class man():
    def __init__(self, name = "Nikita", job = None, car = None):
        self.energy = 300
        self.job = job
        self.money = 300
        self.car = car

class car:
    def __init__(self):
        self.brand = random.choice(list[cars])
        self.fuel = cars[self.brand]["fuel"]
        self.speed = cars[self.brand]["speed"]


class job:
    def __init__(self):
        self.job = random.choice(list(jobs))
        self.money = jobs[self.job]["money"]
        self.energy = jobs[self.job]["energy"]

class chill:
    def __init__(self):
        self.chill = random.choice(list(chill))
        self.money = chill[self.chill]["money"]
        self.energy = chill[self.chill]["energy"]

