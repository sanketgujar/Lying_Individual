import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def update_belief(patterns,z,position,messages,belief,w):
	new_belief = [0]*len(belief)
	norm = 0 
	for pattern in range(0,len(patterns)):
		print (' pattern : ' , patterns[pattern] )
		bel_bar =  belief[pattern]
		print ('bel_bar :' , bel_bar)
		for message in range(0,len(messages)):
			bel_bar *= messages[message][pattern]
		print ('bel_bar after messages:' , bel_bar)
		print ('pattern ', pattern , ' position: ' ,position)
		print ('patterns ' ,patterns[pattern][position])
		
		#sensing update
		new_belief[pattern] = bel_bar
		new_belief[pattern] *= (1-w) if (z == patterns[pattern][position]) else w
		# new_belief[pattern] = bel_bar*patterns[pattern][position]
		# new_belief[pattern]= bel_bar
		print ('new_belief ' , new_belief)
		norm += new_belief[pattern]
		print ('*****************\n')
	new_belief =  list(map(lambda bel:bel/norm , new_belief))
	return new_belief


if __name__ =='__main__':
	belief_final = []
	patterns = [[0,1,0,1],[1,0,1,0],[0,1,1,0]]
	for position in range(len(patterns[0])):
		print ('\n\n ********######***####********** \n\n')
		print ('At position  : ' , position )
		# position = 1
		z = 0
		w = 0.75
		messages = [[0.3,0.1,0.6],[0.5,0.2,0.3],[0.7,0.1,0.2]]
		belief   = [0.45,0.1,0.45]
		new_belief = update_belief(patterns ,z , position , 
			messages , belief , w)
		print (list(new_belief))
		belief_final.append(new_belief)
	
	fig = plt.figure()
	xs  = range(len(patterns)) #as there are 3 patterns
	print (xs)
	ys  = belief_final
	# print (ys)
	ax = fig.add_subplot(111, projection='3d')
	for c, z in zip(['r', 'g', 'b','y'], [3,2, 1, 0]):
	    cs = [c] * len(xs)
	    cs[0] = 'c'
	    ax.bar(xs, ys[z], zs=z, zdir='y', color=cs, alpha=0.8)

	ax.set_xlabel('Pattern') 
	ax.set_ylabel('Position')
	ax.set_zlabel('belief')

	plt.show()