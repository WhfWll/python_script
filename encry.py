import sys

origin_str = sys.argv[1]
encry_str = ''
for i in origin_str:
	encry_str += chr(ord(i) + 6)

print encry_str
