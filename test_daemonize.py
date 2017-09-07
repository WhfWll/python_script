import sys, os, time
def daemonize():
	try: 
		pid=os.fork()
		if pid > 0:
			sys.exit(0)
	except OSError, e:
		sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
		sys.exit(1)

	os.chdir("/")
	os.setsid()
	os.umask(0)
	
	try:
		pid=os.fork()
		if pid > 0:
			print "main process"
			sys.exit(0)	
	except OSError, e: 
            sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
	sys.exit(1)

daemonize()	
f=open('/home/whf/a.txt', 'w')
while True:
	f.write('aaaa')
	f.flush()
	time.sleep(3)
