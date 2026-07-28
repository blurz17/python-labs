def count_vowels(s: str):
    s = s.lower()
    vowels = "aeiou"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    return count


def find_i_location(s: str):
    index = 0

    for ch in s:
        if ch == 'i':
            return f"Found 'i' at index {index}"
        index += 1

    return "'i' not found"


def longest(inputArray: list):
    if not inputArray:
        return []

    longest = max(len(s) for s in inputArray)

    return [s for s in inputArray if len(s) == longest]


def min_boxes(apples, boxes):
    total_apples = sum(apples)

    boxes.sort(reverse=True)

    current_capacity = 0
    count = 0

    for box in boxes:
        current_capacity += box
        count += 1

        if current_capacity >= total_apples:
            return count
        print(count)


if __name__ == "__main__":
    print(count_vowels("BONUS"))

    find_i_location("string")

    print(longest(["aba", "aa", "ad", "vcd", "aba"]))

    print(min_boxes([2, 3, 1], [4, 2, 3, 1]))
