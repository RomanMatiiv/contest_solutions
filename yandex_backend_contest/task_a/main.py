from solution import Robot

r = Robot((0, 0))
print(r.move('NENW'))
print(*r.path())