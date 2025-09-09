def merge(arr:list[int], s:int, e:int):
	
	m = (s + e) // 2

	# arr[s..m] and arr[m+1...e] is sorted
	# we want to merge the two halves of arr
	# such that arr[s...e] becomes sorted

	i = s
	j = m + 1

	out = []

	while i <= m and j <= e:
		if arr[i] <= arr[j]:
			out.append(arr[i])
			i += 1
		else:
			out.append(arr[j])
			j += 1

	while i <= m:
		out.append(arr[i])
		i += 1

	while j <= e:
		out.append(arr[j])
		j += 1


	arr[s:e+1] = out



def merge_sort(arr:list[int], s:int, e:int)->None:
	# base case
	if s == e:
		return

	# recursive case

	# f(s, e) : merge sort the arr[s...e]

	m = (s + e) // 2
	merge_sort(arr, s, m)
	merge_sort(arr, m+1, e)
	merge(arr, s, e)


arr = [60, 50, 40, 30, 20, 10]
merge_sort(arr, 0, len(arr)-1)
print(arr)