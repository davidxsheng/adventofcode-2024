import collections
import os


def parse_input_file(file_path: str) -> tuple[list[int], list[int]]:
    with open(file_path) as file:
        lines = file.readlines()
    list_1 = []
    list_2 = []
    for line in lines:
        val_1, val_2 = line.split("   ")
        list_1.append(int(val_1.strip()))
        list_2.append(int(val_2.strip()))
    return list_1, list_2


def get_list_difference(list_1: list[int], list_2: list[int]) -> int:
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    total_difference = 0
    for val_1, val_2 in zip(sorted_list_1, sorted_list_2):
        total_difference += abs(val_1 - val_2)

    return total_difference


def get_list_similarity(list_1: list[int], list_2: list[int]) -> int:
    list_2_counter = collections.Counter(list_2)
    total_similarity = 0
    for val in list_1:
        total_similarity += val * list_2_counter.get(val, 0)
    return total_similarity


def main() -> int:
    current_path = os.path.realpath(__file__)
    input_file_path = os.path.join(os.path.dirname(current_path), "input.txt")
    list_1, list_2 = parse_input_file(input_file_path)
    print(f"Total difference: {get_list_difference(list_1, list_2)}")
    print(f"Total similarity: {get_list_similarity(list_1, list_2)}")


if __name__ == "__main__":
    main()
