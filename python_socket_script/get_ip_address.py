import socket
import fcntl
import struct
import sys

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	ip_address = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])
	return ip_address

if __name__ == '__main__':
	if sys.argv:
		print get_ip_address(sys.argv[1])
	else:
		print get_ip_address('eth0')
