
class PearsBasket:
    def __init__(self, n: int):
        self.n = n

    # +
    def __add__(self, other):
        new_n = self.n + other.n

        return PearsBasket(new_n)

    # -
    def __sub__(self, number: int):
        self.n -= number

        if self.n < 0:
            self.n = 0

    # //
    def __floordiv__(self, number: int):
        pears_per_basket = self.n // number
        basket = [PearsBasket(pears_per_basket) for _ in range(number)]

        last_basket = self.n % number
        if last_basket != 0:
            basket.append(PearsBasket(last_basket))

        return basket

    # %
    def __mod__(self, number: int):
        return self.n % number

    def __str__(self):
        return str(self.n)

    def __repr__(self):
        return f"PearsBasket({self.n})"