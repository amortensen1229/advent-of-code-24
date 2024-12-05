from typing import List, Tuple
from functools import reduce
from enum import Enum

CHARACTER_SEQUENCE = ["X", "M", "A", "S"]


class Direction(Enum):
    UPPER_LEFT = 1
    UPPER_CENTER = 2
    UPPER_RIGHT = 3

    MID_LEFT = 4
    MID_RIGHT = 5

    LOWER_LEFT = 6
    LOWER_CENTER = 7
    LOWER_RIGHT = 8


def find_character_sequences(character_grid):
    found_sequences = 0
    for row, value in enumerate(character_grid):
        for column, value in enumerate(character_grid[row]):
            if character_grid[row][column] == "X":
                found_sequences += search_area_for_character_sequence(
                    character_grid, row, column, 1, None
                )
    print(found_sequences)


def search_area_for_character_sequence(
    character_grid: List[List[str]],
    row: int,
    column: int,
    sequence_offset: int,
    current_direction: Direction,
) -> int:
    total_found = 0
    if sequence_offset == len(CHARACTER_SEQUENCE):
        return 1
    if check_upper_left(
        character_grid, row, column, sequence_offset, current_direction
    ):
        total_found += search_area_for_character_sequence(
            character_grid,
            row - 1,
            column - 1,
            sequence_offset + 1,
            Direction.UPPER_LEFT,
        )

    if check_upper_center(
        character_grid, row, column, sequence_offset, current_direction
    ):
        total_found += search_area_for_character_sequence(
            character_grid, row - 1, column, sequence_offset + 1, Direction.UPPER_CENTER
        )

    if check_upper_right(
        character_grid, row, column, sequence_offset, current_direction
    ):
        total_found += search_area_for_character_sequence(
            character_grid,
            row - 1,
            column + 1,
            sequence_offset + 1,
            Direction.UPPER_RIGHT,
        )

    if check_mid_left(character_grid, row, column, sequence_offset, current_direction):
        total_found += search_area_for_character_sequence(
            character_grid, row, column - 1, sequence_offset + 1, Direction.MID_LEFT
        )

    if check_mid_right(character_grid, row, column, sequence_offset, current_direction):
        total_found += search_area_for_character_sequence(
            character_grid, row, column + 1, sequence_offset + 1, Direction.MID_RIGHT
        )

    if check_lower_left(
        character_grid, row, column, sequence_offset, current_direction
    ):
        total_found += search_area_for_character_sequence(
            character_grid,
            row + 1,
            column - 1,
            sequence_offset + 1,
            Direction.LOWER_LEFT,
        )

    if check_lower_center(
        character_grid, row, column, sequence_offset, current_direction
    ):
        total_found += search_area_for_character_sequence(
            character_grid, row + 1, column, sequence_offset + 1, Direction.LOWER_CENTER
        )

    if check_lower_right(
        character_grid, row, column, sequence_offset, current_direction
    ):
        total_found += search_area_for_character_sequence(
            character_grid,
            row + 1,
            column + 1,
            sequence_offset + 1,
            Direction.LOWER_RIGHT,
        )
    return total_found


def check_upper_left(
    character_grid: List[List[str]],
    row: int,
    column: int,
    sequence_offset: int,
    last_direction: Direction,
) -> bool:
    if last_direction != Direction.UPPER_LEFT and last_direction != None:
        return False
    if row - 1 < 0 or column - 1 < 0:
        return False

    return character_grid[row - 1][column - 1] == CHARACTER_SEQUENCE[sequence_offset]


def check_upper_center(
    character_grid: List[List[str]],
    row: int,
    column: int,
    sequence_offset: int,
    last_direction: Direction,
) -> bool:
    if last_direction != Direction.UPPER_CENTER and last_direction != None:
        return False
    if row - 1 < 0:
        return False

    return character_grid[row - 1][column] == CHARACTER_SEQUENCE[sequence_offset]


def check_upper_right(
    character_grid: List[List[str]],
    row: int,
    column: int,
    sequence_offset: int,
    last_direction: Direction,
) -> bool:
    if last_direction != Direction.UPPER_RIGHT and last_direction != None:
        return False
    if row - 1 < 0 or column + 1 >= len(character_grid[row - 1]):
        return False

    return character_grid[row - 1][column + 1] == CHARACTER_SEQUENCE[sequence_offset]


def check_mid_left(
    character_grid: List[List[str]],
    row: int,
    column: int,
    sequence_offset: int,
    last_direction: Direction,
) -> bool:
    if last_direction != Direction.MID_LEFT and last_direction != None:
        return False
    if column - 1 < 0:
        return False

    return character_grid[row][column - 1] == CHARACTER_SEQUENCE[sequence_offset]


def check_mid_right(
    character_grid: List[List[str]],
    row: int,
    column: int,
    sequence_offset: int,
    last_direction: Direction,
) -> bool:
    if last_direction != Direction.MID_RIGHT and last_direction != None:
        return False
    if column + 1 >= len(character_grid[row]):
        return False

    return character_grid[row][column + 1] == CHARACTER_SEQUENCE[sequence_offset]


def check_lower_left(
    character_grid: List[List[str]],
    row: int,
    column: int,
    sequence_offset: int,
    last_direction: Direction,
) -> bool:
    if last_direction != Direction.LOWER_LEFT and last_direction != None:
        return False
    if row + 1 >= len(character_grid) or column - 1 < 0:
        return False

    return character_grid[row + 1][column - 1] == CHARACTER_SEQUENCE[sequence_offset]


def check_lower_center(
    character_grid: List[List[str]],
    row: int,
    column: int,
    sequence_offset: int,
    last_direction: Direction,
) -> bool:
    if last_direction != Direction.LOWER_CENTER and last_direction != None:
        return False
    if row + 1 >= len(character_grid):
        return False

    return character_grid[row + 1][column] == CHARACTER_SEQUENCE[sequence_offset]


def check_lower_right(
    character_grid: List[List[str]],
    row: int,
    column: int,
    sequence_offset: int,
    last_direction: Direction,
) -> bool:
    if last_direction != Direction.LOWER_RIGHT and last_direction != None:
        return False
    if (row + 1 >= len(character_grid)) or (column + 1 >= len(character_grid[row + 1])):
        return False

    return character_grid[row + 1][column + 1] == CHARACTER_SEQUENCE[sequence_offset]


def parse_file() -> List[List[str]]:
    character_grid = []

    file = open("input.txt", "r")
    for line in file:
        character_line = []
        for character in line:
            if character == "\n":
                continue
            character_line.append(character)

        character_grid.append(character_line)
    return character_grid


if __name__ == "__main__":
    character_grid: List[List[str]] = parse_file()
    print(character_grid)
    find_character_sequences(character_grid)

    ##print(f"Total Value: {compute_mul_operations(mul_operations)}")
