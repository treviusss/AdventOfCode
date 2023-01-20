from day4_part2 import Solution

is_overlapping = Solution.is_overlapping
# .234.....  2-4
# .....678.  6-8

# .23......  2-3
# ...45....  4-5

# ....567..  5-7
# ......789  7-9

# .2345678.  2-8
# ..34567..  3-7

# .....6...  6-6
# ...456...  4-6

# .....6...  6-6
# .....678.. 6-8

# .23456...  2-6
# ...45678.  4-8

data = {
    (2, 4, 6, 8): False,
    (2, 3, 4, 5): False,
    (5, 7, 7, 9): True,
    (5, 7, 3, 5): True,
    (2, 8, 3, 7): True,
    (6, 6, 4, 6): True,
    (6, 6, 6, 8): True,
    (2, 6, 4, 8): True,
    (9, 27, 10, 80): True,
}


def test_is_overlapping():
    for item, answer in data.items():
        assert is_overlapping(*item) == answer
