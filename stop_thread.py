import time
import threading

def doit(arg):
	t = threading.currentThread()
	while getattr(t, 'do_run', True):
		print('Working')
		time.sleep(1)
	print('Stop')

def main():
	t = threading.Thread(target=doit, args=('ac', ))
	t.start()
	time.sleep(10)
	t.do_run = False
	t.join()

if __name__=='__main__':
	main()
