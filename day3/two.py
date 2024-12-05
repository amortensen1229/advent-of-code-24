import re
from typing import List, Tuple
from functools import reduce
from enum import Enum

class Operation(Enum):
    ENABLE = 1
    DISABLE = 2


class MulOperationIndex:
    def __init__(self, operation_type: Operation, index: int):
        self.operation_type = operation_type
        self.index = index

    def __str__(self):
        return f"Operation: {self.operation_type}, Index: {self.index}"
    
    def __repr__(self):
        return f"Operation: {self.operation_type}, Index: {self.index}\n"



def compute_mul_operations(mul_operations: List[Tuple[int, int]]) -> int:
    return reduce(lambda a,b: a+b, (mul_operation[0] * mul_operation[1] for mul_operation in mul_operations))

def compute_disabled_windows() -> List[Tuple[int, int]]:
    file = open("input.txt", "r")
    enabled_indexes, disabled_indexes = get_enabled_disabled_indexes(file)
    return reduce_to_closed_windows(disabled_indexes=disabled_indexes, enabled_indexes=enabled_indexes)
            
def get_enabled_disabled_indexes(file) -> Tuple[List[int], List[int]]:
    enabled_values = []
    disabled_values = []
    enabled_pattern = r"do\(\)"
    disabled_pattern = r"don't\(\)"
    file_offset = 0
    for line in file:
        do_matches = re.finditer(enabled_pattern, line)
        dont_matches = re.finditer(disabled_pattern, line)
        for dont_match in dont_matches:
            disabled_values.append(file_offset + dont_match.span()[1])
        for do_match in do_matches:
            enabled_values.append(file_offset + do_match.span()[1])
        file_offset += len(line)
    return (enabled_values, disabled_values)


def reduce_to_closed_windows(disabled_indexes: List[int], enabled_indexes: List[int]) -> List[Tuple[int, int]]:
    closed_windows = []

    all_windows: List[MulOperationIndex] = []
    for disabled_index in disabled_indexes:
        all_windows.append(MulOperationIndex(Operation.DISABLE, disabled_index))
    
    for enabled_index in enabled_indexes:
        all_windows.append(MulOperationIndex(Operation.ENABLE, enabled_index))
  
    mul_enabled = True
    all_windows_sorted = sorted(all_windows, key=lambda mul_operation_index: mul_operation_index.index)
    print(all_windows_sorted)
    closed_window_start = 0
    for i, window in enumerate(all_windows_sorted):
        if (window.operation_type == Operation.DISABLE and mul_enabled == True):
            mul_enabled = False
            closed_window_start = window.index
        
        if (window.operation_type == Operation.ENABLE and mul_enabled == False):
            mul_enabled = True
            closed_windows.append((closed_window_start, window.index))

    print(closed_windows)
    return closed_windows
      

def is_value_in_closed_window(closed_windows: List[Tuple[int, int]], value: int) -> bool:
    for closed_window in closed_windows:
        if (closed_window[0] < value and closed_window[1] > value):
            return True
    return False


## Numbers in input file are int sized
def parse_file() -> List[Tuple[int, int]]:
    file = open("input.txt", "r")
    closed_windows = compute_disabled_windows() 

    mul_pattern = r"mul\(\s*(?P<X>-?\d+)\s*,\s*(?P<Y>-?\d+)\s*\)"
    mul_operations = []
    file_offset = 0
    for line in file:
        mul_matches = re.finditer(mul_pattern, line)
        for match in mul_matches:
            match_start_index = match.span()[0]
            if (is_value_in_closed_window(closed_windows=closed_windows, value=(file_offset + match_start_index))):
                continue
            mul_operations.append((int(match.group("X")), int(match.group("Y"))))
        file_offset += len(line)
    return mul_operations


if __name__ == "__main__":
    mul_operations: List[Tuple[int, int]] = parse_file()
    print(f"Total Value With Enabled/Disabled Windows: {compute_mul_operations(mul_operations)}")