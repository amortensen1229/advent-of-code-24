from typing import List, Tuple
from functools import reduce

MAX_LEVEL_DIFFERENCE = 3
MIN_LEVEL_DIFFERENCE = 1


def count_safe_reports_with_removal(reports: List[List[int]]) -> int:
    return reduce(
        lambda a, b: a + b,
        (1 if is_safe_report_with_removal(report) else 0 for report in reports),
    )


def is_safe_report_with_removal(report: List[int]) -> bool:
    for i in range(len(report)):
        levels_with_removal = [item for index, item in enumerate(report) if index != i]
        if (
            report_is_continuously_decreasing(levels_with_removal)
            or report_is_continuously_increasing(levels_with_removal)
        ) and report_intervals_differ_by_acceptable_amounts(levels_with_removal):
            return True

    return False


def report_is_continuously_increasing(report: List[int]) -> bool:
    previous_level = report[0]
    for level in report[1:]:
        if previous_level <= level:
            return False
        previous_level = level

    return True


def report_is_continuously_decreasing(report: List[int]) -> bool:
    previous_level = report[0]
    for level in report[1:]:
        if previous_level >= level:
            return False
        previous_level = level

    return True


def report_intervals_differ_by_acceptable_amounts(report: List[int]) -> bool:
    previous_level = report[0]
    for level in report[1:]:
        level_delta = abs(previous_level - level)
        if level_delta > MAX_LEVEL_DIFFERENCE or level_delta < MIN_LEVEL_DIFFERENCE:
            return False
        previous_level = level

    return True


## Numbers in input file are int sized
def parse_file() -> List[List[int]]:
    file = open("reports.txt", "r")
    reports = []
    for line in file:
        reports.append(list(map(int, line.strip().split())))
    return reports


if __name__ == "__main__":
    reports: List[List[int]] = parse_file()
    print(f"Safe Report Count: {count_safe_reports_with_removal(reports)}")
