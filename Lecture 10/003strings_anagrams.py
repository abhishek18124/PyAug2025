# assume s and t are of equal length n

# time : n steps to build fmap_s + n steps to build fmap_t + 26 to do comparision of fmap_s and fmap_t
# time : 2n + 26 ~ O(n)
# space: 26 + 26 due to fmap_s and fmap_t ~ O(1)

def is_anagram(s:str, t:str)->bool:
	fmap_s = [0] * 26
	for ch in s:
		idx = ord(ch) - ord('a')
		fmap_s[idx] += 1

	print(fmap_s)

	fmap_t = [0] * 26
	for ch in t:
		idx = ord(ch) - ord('a')
		fmap_t[idx] += 1
	
	print(fmap_t)

	# return fmap_s == fmap_t

	for i in range(26):
		if fmap_s[i] != fmap_t[i]:
			return False # s and t are not anagrams

	# s and t are anagrams
	return True


s = "state"
t = "taste"

print(is_anagram(s, t))

# print(ord('a') - ord('a'))
# print(ord('b') - ord('a'))
# print(ord('c') - ord('a'))

# # a->0, b->1, c->2, d->3, ...