class Robot:
    def __init__(self, start_position):
        self.x = start_position[0]
        self.y = start_position[1]
        self._path = list()

        self._add_cur_position_to_path()

    def move(self, commands: str):
        for cur_cmd in commands:
            if cur_cmd == "N":
                self._up()
            elif cur_cmd == "S":
                self._down()
            elif cur_cmd == "E":
                self._right()
            elif cur_cmd == "W":
                self._left()
            else:
                raise ValueError

            self._add_cur_position_to_path()

        finish_position = (self.x, self.y)

        return finish_position

    def path(self):
        cur_pah = self._path
        self._path = list([cur_pah[-1]])

        return cur_pah

    def _up(self):
        self.y += 1

    def _down(self):
        self.y -= 1

    def _right(self):
        self.x += 1

    def _left(self):
        self.x -= 1

    def _add_cur_position_to_path(self):
        cur_position = (self.x, self.y)
        self._path.append(cur_position)
