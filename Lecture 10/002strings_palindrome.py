# time : n/2.const ~ O(n)
# space: O(1)

def is_palindrome(s:str)->bool:
	i = 0
	j = len(s) - 1
	while i < j:
		if s[i] == s[j]:
			i += 1
			j -= 1
		else:
			# given string is not a palindrome
			return False
	# given string a palindrome
	return True


s = input()
print(is_palindrome(s))