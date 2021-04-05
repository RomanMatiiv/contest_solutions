from math import inf

from solution import Cart
from solution import Vehicle
from solution import Bike


class Winner:
    def __init__(self, num, delta_to_finish):
        self.num = num
        self.delta_to_finish = delta_to_finish


if __name__ == "__main__":
    n, m, t = [int(i) for i in input().split()]

    dist = t * m
    winner = Winner(num=None, delta_to_finish=inf)

    for _ in range(n):
        cur_descr = [int(i) for i in input().split()]

        number = cur_descr[0]
        trans_type = cur_descr[1]
        speed = cur_descr[2]

        if trans_type == 1:
            cur_transport = Vehicle(number, speed, petrol=cur_descr[3])
        elif trans_type == 2:
            cur_transport = Bike(number, speed, petrol=cur_descr[3])
        elif trans_type == 3:
            cur_transport = Cart(number, speed)
        else:
            raise ValueError

        cur_transport_dist = cur_transport.get_speed() * t
        # cur_delta_to_finish = abs(cur_transport_dist - m * t)

        cur_delta_to_finish_raw = cur_transport_dist % m
        cur_delta_to_finish = min(cur_delta_to_finish_raw, m - cur_delta_to_finish_raw)

        if cur_delta_to_finish < winner.delta_to_finish:
            winner.num = cur_transport.get_gos_number()
            winner.delta_to_finish = cur_delta_to_finish
        elif (cur_delta_to_finish == winner.delta_to_finish and
                winner.num > cur_transport.get_gos_number()):
            winner.num = cur_transport.get_gos_number()
            winner.delta_to_finish = cur_delta_to_finish
    print(winner.num)
