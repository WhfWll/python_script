import sys
import os
import re
import pdb

def main():
	try:
		dirname = sys.argv[1]
		key_word = sys.argv[2]
	except:
		print 'need dir or keyword.'
		return ''
	keyword = re.compile(key_word)
	for parent,dirnames,filenames in os.walk(dirname):
		for dirname in dirnames:
			pass
		for filename in filenames:
			if parent[-1] != '/':
				file_path = parent + '/' + filename
			else:
				file_path = parent + filename
			f = file(file_path, 'r').read()
			if keyword.search(f):
				print file_path
	


if __name__ == "__main__":
	main()
