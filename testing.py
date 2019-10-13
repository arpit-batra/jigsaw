import numpy as np
import math

# a=np.load("pieces.npy")

#Euclidean distance between two 3dimensional points
def EucDistance(point1,point2):
	result=0
	for i in range(3):
		result+=(point1[i]-point2[i])**2
	return math.sqrt(result)


def patchDiff(patch1,patch2):
	ans=0	
	for i in range(patch1.shape[0]):
		for j in range(patch1.shape[1]):
			ans+=EucDistance(patch1[i][j],patch2[i][j])
	return ans

def testing(a):
	i=0
	for j in range(a.shape[1]):

		count = 0
		for k in range(a.shape[0]):
			for l in range(a.shape[1]):
				if(i!=k or j!=l):
					if(patchDiff(a[i][j],a[k][l])<1e-6):
						count += 1
		print(str(i) + ", " + str(j) + " - " + str(count))
