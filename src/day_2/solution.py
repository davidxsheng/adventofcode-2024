import os
import time


def parse_input_file(file_path: str) -> list[list[int]]:
    """Parse the input txt file."""
    with open(file_path) as file:
        lines = file.readlines()
    processed_lines: list[list[int]] = []
    for line in lines:
        processed_line = [int(val) for val in line.strip().split(" ")]
        processed_lines.append(processed_line)
    return processed_lines


def is_safe(report: list[int]) -> bool:
    """Test if the report is safe.

    A report is safe if the its numbers are monotonically increasing or decreasing
    and the difference between each element is less than or equal to 3.

    :param report: a list of integers
    :return: True if the report is safe with a dampener, False otherwise
    """
    if len(report) <= 1:
        return True
    differences = [report[i] - report[i - 1] for i in range(1, len(report))]
    return all(diff <= 3 and diff > 0 for diff in differences) or all(
        diff < 0 and diff >= -3 for diff in differences
    )


def is_safe_with_dampener(report: list[int]) -> bool:
    """Test if the report is safe with a dampener.

    A report is safe with a dampener if it is safe with up to one
    element removed from it.

    :param report: a list of integers
    :return: True if the report is safe with a dampener, False otherwise
    """
    if len(report) <= 1 or is_safe(report[1:]):
        return True
    is_increasing = report[1] > report[0]
    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]
        if is_increasing:
            if difference <= 0 or difference > 3:
                return is_safe(report[:i] + report[i + 1 :]) or is_safe(
                    report[: i - 1] + report[i:]
                )
        else:
            if difference >= 0 or difference < -3:
                return is_safe(report[:i] + report[i + 1 :]) or is_safe(
                    report[: i - 1] + report[i:]
                )
    return True


def is_safe_with_dampener_brute_force(report: list[int]) -> bool:
    """Test if the report is safe with a dampener.

    A report is safe with a dampener if it is safe with up to one
    element removed from it.

    :param report: a list of integers
    :return: True if the report is safe with a dampener, False otherwise
    """
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True
    return False


def main() -> None:
    current_path = os.path.realpath(__file__)
    input_file_path = os.path.join(os.path.dirname(current_path), "input.txt")
    processed_lines = parse_input_file(input_file_path)
    start = time.perf_counter()
    total_safe_lines = sum(is_safe(report) for report in processed_lines)
    end = time.perf_counter()
    print(f"Total safe lines: {total_safe_lines}. Time taken: {end - start}")

    start = time.perf_counter()
    total_safe_lines = sum(is_safe_with_dampener(report) for report in processed_lines)
    end = time.perf_counter()
    print(
        f"Total safe lines with dampener: {total_safe_lines}. Time taken: {end - start}"
    )

    start = time.perf_counter()
    total_safe_lines = sum(
        is_safe_with_dampener_brute_force(report) for report in processed_lines
    )
    end = time.perf_counter()
    print(
        f"Total safe lines with dampener (brute force): {total_safe_lines}. Time taken: {end - start}"
    )


if __name__ == "__main__":
    main()
