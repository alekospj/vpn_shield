import time
import subprocess
from multiprocessing import Process
import socket        
		
		
		
		
if __name__ == "__main__":	

	
	ip = socket.gethostbyname(socket.gethostname())
    #Setting here the program tha you want to close when a changing of an IP is detected. 
	program_loc = r"C:\Users\xoxlios\Desktop\uTorrent\uTorrent.exe"
	
	def open_program(path_name):
		return subprocess.Popen(path_name)
        
	p = open_program(program_loc) 

	

	while True:
		if ip == socket.gethostbyname(socket.gethostname()):
			print('Conected at:',ip)
			time.sleep(1)
		else:
			print('ip changed!')
			p.terminate()
			break
