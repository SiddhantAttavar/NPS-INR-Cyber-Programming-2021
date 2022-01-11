t, m = input().split()
for _ in range(int(t)):
	l = input()
	res = ''
	for c in l:
		if c.isalpha():
			if c.isupper():
				res += m[ord(c) - ord('A')].upper()
			else:
				res += m[ord(c) - ord('a')].lower()
		else:
			res += c
	res = res.replace('_', ' ')
	print(res)
