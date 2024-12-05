from functools import reduce
from typing import List, Tuple


def calculate_similarity(location_id_lists: Tuple[List[int], List[int]]) -> int:
    reference_list = location_id_lists[0]
    search_list = location_id_lists[1]
    reference_occurrence_dict = {
        reference_value: (lambda ref_value: search_list.count(ref_value))(
            reference_value
        )
        for reference_value in reference_list
    }

    return reduce(
        lambda a, b: a + b,
        (
            ref_value * reference_occurrence_dict[ref_value]
            for ref_value in reference_list
        ),
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
    print(f"Similiarity Socre: {calculate_similarity(location_id_lists)}")
