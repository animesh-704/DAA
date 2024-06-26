def find(i): 

	# If i is the parent of itself 
	if Parent[i] == i: 

		# Then i is the representative 
		return i 
	else: 

		# Recursively find the representative. 
		result = find(Parent[i]) 

		# We cache the result by moving i’s node 
		# directly under the representative of this 
		# set 
		Parent[i] = result 
		
		# And then we return the result 
		return result
