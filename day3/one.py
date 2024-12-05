import re
from typing import List, Tuple
from functools import reduce


def compute_mul_operations(mul_operations: List[Tuple[int, int]]) -> int:
    return reduce(lambda a,b: a+b, (mul_operation[0] * mul_operation[1] for mul_operation in mul_operations))


## Numbers in input file are int sized
def parse_file() -> List[Tuple[int, int]]:
    pattern = r"mul\(\s*(?P<X>-?\d+)\s*,\s*(?P<Y>-?\d+)\s*\)"
    file = open("input.txt", "r")
    mul_operations = []
    for line in file:
        matches = re.finditer(pattern, line)
        for match in matches:
            mul_operations.append((int(match.group("X")), int(match.group("Y"))))
    return mul_operations


if __name__ == "__main__":
    mul_operations: List[Tuple[int, int]] = parse_file()
    print(f"Total Value: {compute_mul_operations(mul_operations)}")
