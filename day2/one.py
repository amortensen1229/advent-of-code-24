from typing import List, Tuple
from functools import reduce

MAX_LEVEL_DIFFERENCE = 3
MIN_LEVEL_DIFFERENCE = 1


def count_safe_reports(reports: List[List[int]]) -> int:
    return reduce(
        lambda a, b: a + b, (1 if is_safe_report(report) else 0 for report in reports)
    )


def is_safe_report(report: List[int]) -> bool:
    return (
        report_is_continuously_decreasing(report)
        or report_is_continuously_increasing(report)
    ) and report_intervals_differ_by_acceptable_amounts(report)


def report_is_continuously_increasing(report: List[int]) -> bool:
    previous_level = report[0]
    for level in report[1:]:
        if previous_level <= level:
            print(f"Previous: {previous_level}, Current: {level}\n")
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
    print(f"Safe Report Count: {count_safe_reports(reports)}")
