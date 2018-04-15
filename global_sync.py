#*******************************
#SWARM INTELLIGENCE HW 2 PROBLEM 1
#Saket Gujar (srgujar@wpi.edu)
#*******************************

import numpy as np 
import cv2
from time import sleep
import time
import matplotlib.pyplot as plt
class global_sync():
	def __init__(self , N = 20 , T = 100 , k = 0.5):
		self.N  = N  #no of agents.
		self.T  = T  #maximum value the counter can assume.
		self.k  = k  #constant between [0,1]
		self.env = np.zeros(N)
		self.c  = np.random.randint(self.T , size = N)
		self.n_iteration = 10000
		self.global_sync()
		# time_m = []
		# for self.k in np.arange(0.1 , 1.01 , 0.01):
			# print ('For k value  =  : ' , self.k )
			# time_m.append(self.global_sync())
		# plt.plot(np.arange(0.1,1.01,0.01) , time_m )
		# plt.xlabel('Value of k')
		# plt.ylabel('Mean Flash time')
		# plt.show()

	def neighbour_flashed(self , idx):
		left_idx = (((idx - 1) + (self.N) ) % self.N)
		right_idx = ((idx + 1) % (self.N ))
		# print ('left_id :' , left_idx , 'id: ' , idx , ' right id : ', right_idx)
		if ((self.env[left_idx] == 1 ) or (self.env[right_idx] == 1 ) ):
			return 1 #if one of the neighbour flashed return 1
		return 0

	def global_sync(self):
		prev_time = time.time()
		flash_count  = 0
		mean_time = 0
		for it in range(self.n_iteration):
			self.display()
			#check all the agents neighbours state
			for i in range(self.N): #total no_of_agents
				if(self.neighbour_flashed(i)):
					self.c[i] += self.c[i]*self.k 
				else:
					self.c[i] += 1

				if (self.c[i] >= self.T):
					self.env[i] = 1
					self.c[i]   = 0
				else:
					self.env[i] = 0
		# 	if (sum(self.env[self.env == 1]) >= 18):
		# 		# print ('completely flashed')
		# 		time_delta = (time.time() - prev_time)
		# 		prev_time  =  time.time() 
		# 		# print ('The time_difference of the ' , flash_count , ' flash is :' , time_delta)
		# 		flash_count += 1
		# 		if (flash_count > 2):
		# 			mean_time += time_delta
		# print ('Mean Flash time for value of k = ', self.k , ' is ' , (mean_time / (flash_count -2)) )	
		# return mean_time
		# print ('Completed iterations')

	def display(self,display_size = (100,1600) , print_state =  True):
		if print_state:
			print ('Current_state  : ' , self.env)
		disp = np.zeros((display_size[0] , display_size[1] , 3 ))
		#each unit will have (d_s[1]/N , d_s[1] )
		f_box = int (display_size[1] / self.N)
		for i in range(self.N):
			if (self.env[i] == 1):
				disp[ : ,i*f_box : (i+1)*f_box ] = [0,255,255] #Yellow
			else:
				disp[ : ,i*f_box : (i+1)*f_box ] = [0 ,0 ,0 ]  #Black
		cv2.imshow('frame' , disp)
		cv2.waitKey(1)
		sleep(0.05)

if __name__ == '__main__':
	syn = global_sync()