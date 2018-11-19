def make_bricks(small, big, goal):
    if goal <= big * 5 + small:
        return small >= goal % 5
    return False

''' Facit
def make_bricks(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - (5 * big)
    else:
        remainder = goal % 5

    return small >= remainder
'''

assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(3, 2, 10) is True
assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(3, 2, 10) is True
assert make_bricks(3, 2, 8) is True
assert make_bricks(3, 2, 9) is False
assert make_bricks(6, 1, 11) is True
assert make_bricks(6, 0, 11) is False
assert make_bricks(1, 4, 11) is True
assert make_bricks(0, 3, 10) is True
assert make_bricks(1, 4, 12) is False
assert make_bricks(3, 1, 7) is True
assert make_bricks(1, 1, 7) is False
assert make_bricks(2, 1, 7) is True
assert make_bricks(7, 1, 11) is True
assert make_bricks(7, 1, 8) is True
assert make_bricks(7, 1, 13) is False
assert make_bricks(43, 1, 46) is True
assert make_bricks(40, 1, 46) is False
assert make_bricks(40, 2, 47) is True
assert make_bricks(40, 2, 50) is True
assert make_bricks(40, 2, 52) is False
assert make_bricks(22, 2, 33) is False
assert make_bricks(0, 2, 10) is True
assert make_bricks(1000000, 1000, 1000100) is True
assert make_bricks(2, 1000000, 100003) is False
assert make_bricks(20, 0, 19) is True
assert make_bricks(20, 0, 21) is False
assert make_bricks(20, 4, 51) is False
assert make_bricks(20, 4, 39) is True
