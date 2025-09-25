from collections import defaultdict, Counter


def is_duplicate_present(arr: list[int]) -> bool:
    freq_map = defaultdict(int)
    for item in arr:
        freq_map[item] += 1
        if freq_map[item] > 1:
            # you've found a duplicate
            return True

    return False  # no duplicate found
    # print(freq_map)


def is_duplicate_present_using_counter(arr: list[int]) -> bool:
    freq_map = Counter(arr)
    for val in freq_map.values():
        if val > 1:
            return True
    return False


arr = [1, 2, 3, 4]
print(is_duplicate_present(arr))

# print(Counter(arr))


print(is_duplicate_present_using_counter(arr))

print(help(Counter))
