import day8_part1 as d8_p1

example_data = """30373
25512
65332
33549
35390"""

example_data = example_data.split("\n")
assert d8_p1.count_visible_trees(example_data) == 21
