animals = ["cheetah", "alpaca", "zebra", "bear"]
sorted_animals = sorted(animals)
print(sorted_animals)
print(animals)

sorted_animals_by_len = sorted(animals, key=len)
print(sorted_animals_by_len)

pairs = [(2, 3), (3, 1), (1, 2)]
sorted_pairs = sorted(pairs)
print(sorted_pairs)


def itemgetter(pair):
	return pair[1]

sorted_pairs_2 = sorted(pairs, key=itemgetter)
print(sorted_pairs_2)

def f(num):
	return -num

nums = [10, 5, 20, 3, 12]
# nums.sort(key=f)
nums.sort(reverse=True)
print(nums)