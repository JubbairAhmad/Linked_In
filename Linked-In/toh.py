def TowerOfHanoi (n, rod1, rod2, rod3): 
	# solved using rescursion method
	if n == 0: 
		return
	TowerOfHanoi(n-1, rod1, rod3, rod2) 
	print("Disk", n, "moved from", rod1, "to", rod3) 
	TowerOfHanoi(n-1, rod3, rod2, rod1) 
	
N = int(input())
TowerOfHanoi(n, 1, 2, 3)
