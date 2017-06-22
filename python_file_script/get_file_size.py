import os
import argparse

def get_file_size(path):
	try:
		size = os.path.getsize(path)
		return format_size(size)
	except Exception as e:
		print e

def get_dir_size(path):
	sumsize = 0
	try:
		filename = os.walk(path)
		for root, dirs, files in filename:
			for fle in files:
				size = os.path.getsize(os.path.join(root, fle))
				sumsize += size
		return format_size(sumsize)
	except Exception as e:
		print e

def format_size(bytes):
	try:
		bytes = float(bytes)
		kb = bytes/1024
	except:
		print 'not a right byte format'
		return 'Error'
	
	if kb >= 1024:
		M = kb/1024
		if M >= 1024:
			G = M/1024
			return '%fG' % G
		else:
			return '%fM' % M
	else:
		return '%fkb' % kb

def parse_args():
	parser = argparse.ArgumentParser('get file or directory size')
	parser.add_argument('-f', help='get a file size')
	parser.add_argument('-d', help='get a directory size')
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parse_args()
	if args.f:
		size = get_file_size(args.f)
		print 'file size: ' + size
	if args.d:
		size = get_dir_size(args.d)
		print 'directory size: ' + size
