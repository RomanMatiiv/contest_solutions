class AbstractCat:
    def __init__(self, weight=0):
        self.weight = weight

        self.previous_eat = 0

    def __str__(self):
        return f"{self.__class__.__name__} ({self.weight})"

    def eat(self, n: int):
        eat_to_weight = 10

        if self.weight != 100:
            cur_eat = n + self.previous_eat

            self.weight += cur_eat // eat_to_weight
            if self.weight > 100:
                self.weight = 100

            self.previous_eat = n % eat_to_weight


class Kitten(AbstractCat):
    def __init__(self, weight):
        super().__init__(weight)

    def meow(self):
        return "meow..."

    def sleep(self):
        weight_to_sleep = 5
        sleep_sound = "Snore"

        n_repeat = self.weight // weight_to_sleep
        return sleep_sound * n_repeat


class Cat(Kitten):
    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name

    def meow(self):
        return super().meow().upper()

    def get_name(self):
        return self.name

    def catch_mice(self):
        return "Got it!"