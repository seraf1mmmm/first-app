import random

cars = {
    "BMW": {"fuel": 100, "speed": 130},
    "jiguli": {"fuel": 80, "speed": 90}
}

jobs = {
    "builder": {"salary": 150, "energy": 100},
    "taxist": {"salary": 70, "energy": 250},
}

chill_places = {
    "home": {"money": 200, "energy": 300},
    "beach": {"money": 300, "energy": 200},
}

class Car:
    def __init__(self):
        self.brand = random.choice(list(cars.keys()))
        self.fuel = cars[self.brand]["fuel"]
        self.speed = cars[self.brand]["speed"]

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 10
            print(f"{self.brand} їде. Паливо залишилось: {self.fuel}")
        else:
            print(f"{self.brand} не має пального!")

class Job:
    def __init__(self):
        self.name = random.choice(list(jobs.keys()))
        self.salary = jobs[self.name]["salary"]
        self.energy_required = jobs[self.name]["energy"]

class Relax:
    def __init__(self):
        self.place = random.choice(list(chill_places.keys()))
        self.money_spent = chill_places[self.place]["money"]
        self.energy_gained = chill_places[self.place]["energy"]

class Man:
    def __init__(self, name="Нікіта", job=None, car=None):
        self.name = name
        self.energy = 300
        self.money = 300
        self.car = car if car else Car()
        self.job = job if job else Job()

    def work(self):
        if self.energy >= self.job.energy_required:
            self.money += self.job.salary
            self.energy -= self.job.energy_required
            print(f"{self.name} працював як {self.job.name} і заробив {self.job.salary}.")
        else:
            print(f"{self.name} занадто втомлений, щоб працювати!")

    def relax(self):
        place = Relax()
        if self.money >= place.money_spent:
            self.money -= place.money_spent
            self.energy += place.energy_gained
            print(f"{self.name} відпочив у {place.place}. Отримано {place.energy_gained} енергії.")
        else:
            print(f"{self.name} не має достатньо грошей, щоб відпочити у {place.place}!")

# Example usage
person = Man()
person.work()
person.relax()
person.car.drive()
