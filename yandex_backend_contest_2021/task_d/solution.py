
class Transport:
    def __init__(self, gos_number, speed):
        self._gos_number = gos_number
        self._speed = speed

    def get_speed(self):
        return self._speed

    def get_gos_number(self):
        return self._gos_number


class TransportWithPetrol(Transport):
    def __init__(self, gos_number, speed, petrol):
        super().__init__(gos_number, speed)

        if petrol not in [98, 95, 92]:
            raise ValueError
        self._petrol = petrol


class Cart(Transport):
    def __init__(self, gos_number, speed):
        super().__init__(gos_number, speed)


class Vehicle(TransportWithPetrol):
    def __init__(self, gos_number, speed, petrol):
        super().__init__(gos_number, speed, petrol)

    def get_speed(self):
        ideal_speed = super().get_speed()
        real_speed = None

        if self._petrol == 98:
            real_speed = ideal_speed
        elif self._petrol == 95:
            real_speed = ideal_speed * 0.9
        elif self._petrol == 92:
            real_speed = ideal_speed * 0.8

        return real_speed


class Bike(TransportWithPetrol):
    def __init__(self, gos_number, speed, petrol):
        super().__init__(gos_number, speed, petrol)

    def get_speed(self):
        ideal_speed = super().get_speed()
        real_speed = None

        if self._petrol == 98:
            real_speed = ideal_speed
        elif self._petrol == 95:
            real_speed = ideal_speed * 0.8
        elif self._petrol == 92:
            real_speed = ideal_speed * 0.6

        return real_speed


