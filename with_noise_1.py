import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def update_belief(patterns,position,messages,belief,observation,
	w):
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
		# new_belief[pattern] = bel_bar*patterns[pattern][position]
		# new_belief[pattern]= bel_bar
		if observation == patterns[pattern][position]:
			match_obs = 1 - w
		else:
			match_obs = w
		new_belief[pattern]  = bel_bar*match_obs
		print ('new_belief ' , new_belief)
		norm += new_belief[pattern]
		print ('*****************\n')
	new_belief =  list(map(lambda bel:bel/norm , new_belief))
	return new_belief


if __name__ =='__main__':
	# belief_final = []
	patterns = [[1,0,1,1],[1,0,1,0],[0,1,1,0]]
	correct_pattern = 2
	observation = patterns[correct_pattern]
	epoch = 10
	# w = 0.01	# print (belief_final.shape)
	correct_value = []
	lenght_of_noise = np.arange(0.,1.,0.01)
	for w in lenght_of_noise:
		belief_final = np.array([[0.333,0.333,0.333],[0.333,0.333,0.333],
			[0.333,0.333,0.333],[0.333,0.333,0.333]])
		correct_prediction = 0
		for ep in range(epoch):
			for position in range(len(patterns[0])):
				print ('\n\n ********##########************* \n\n')
				print ('At position  : ' , position )
				# position = 1
				belief  = belief_final[position]
				messages= np.delete(belief_final,range(position*3,(position+1)*3)).reshape(3,3)
				# print ('messages : ',messages)
				belief_final[position] = update_belief(patterns , position , messages , 
					belief, observation[position],w)
				# print (list(new_belief))
				# belief_final.append(new_belief)
		for i in range(len(belief_final)):
			if (np.argmax(belief_final[i]) == correct_pattern ):
				correct_prediction += 1
		correct_value.append(correct_prediction)
	plt.plot(lenght_of_noise,correct_value,linewidth = 3.3)	
	plt.grid()
	plt.ylabel('No of correct predictions by robots')
	plt.xlabel('noise')
	plt.show()
	# fig = plt.figure()	
	# xs  = range(len(patterns)) #as there are 3 patterns
	# # print (xs)
	# ys  = belief_final
	# # print (ys)
	# ax = fig.add_subplot(111, projection='3d')
	# for c, z in zip(['r', 'g', 'b','y'], [3,2, 1, 0]):
	#     cs = [c] * len(xs)
	#     cs[0] = 'c'
	#     ax.bar(xs, ys[z], zs=z, zdir='y', color=cs, alpha=0.8)

	# ax.set_xlabel('Pattern') 
	# ax.set_ylabel('Position')
	# ax.set_zlabel('belief')

	# plt.show()