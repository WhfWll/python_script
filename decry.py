import sys

decry_str = sys.argv[1]
origin_str = ''

for i in decry_str:
	origin_str += chr(ord(i) - 6)

print origin_str
