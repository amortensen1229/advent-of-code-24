from typing import List, Tuple
from functools import reduce


def number_pair_delta(location_id_lists: Tuple[List[int], List[int]]) -> int:
    ## Sort
    location_id_lists[0].sort()
    location_id_lists[1].sort()

    ## Assuming input would always be equal length, compare each element, then sum
    return reduce(
        lambda a, b: a + b,
        [
            abs(first - second)
            for (first, second) in zip(location_id_lists[0], location_id_lists[1])
        ],
    )


## Numbers in input file are int sized
def parse_file() -> Tuple[List[int], List[int]]:
    file = open("number_pairs.txt", "r")
    first_location_id_list = []
    second_location_id_list = []
    for line in file:
        location_id_pair = line.strip().split()
        first_location_id_list.append(int(location_id_pair[0]))
        second_location_id_list.append(int(location_id_pair[1]))

    return (first_location_id_list, second_location_id_list)


if __name__ == "__main__":
    location_id_lists: Tuple[List[int], List[int]] = parse_file()
    print(f"Total Delta: {number_pair_delta(location_id_lists)}")
