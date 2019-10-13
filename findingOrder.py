import numpy as np

#--------->y
#|
#|
#|
#|
#  x

#Returns Left patch of current patch
def left(currentPatch):
	return currentPatch[0],currentPatch[1]-1

#Returns Right patch of current patch
def right(currentPatch):
	return currentPatch[0],currentPatch[1]+1

#Returns Above patch of current patch
def above(currentPatch):
	return currentPatch[0]-1,currentPatch[1]

#Returns Below patch of current patch
def below(currentPatch):
	return currentPatch[0]+1,currentPatch[1]




#Return Patch Position that should be considered and its side
# 0-Above
# 1-Left
# 2-Below
# 3-Right

def findNext(presentState,currentPatch):
	if(currentPatch==(-1,-1)):
		for i in range(presentState.shape[0]):
			for j in range(presentState.shape[1]-1):
				if(presentState[i][j+1]==1):
					return (i,j),3



	else:
		#print("two")
		rPos=right(currentPatch)
		aPos=above(currentPatch)
		bPos=below(currentPatch)
		lPos=left(currentPatch)
		alPos=above(left(currentPatch))
		arPos=above(right(currentPatch))
		blPos=below(left(currentPatch))
		brPos=below(right(currentPatch))		
		# print("br")
		# print(brPos)
		
		if(presentState[rPos]==1 and presentState[lPos]==1 and presentState[aPos]==1 and presentState[bPos]==1):
			# print("In the hole")
			return ((-1,-1),3)

		if(rPos[1]<presentState.shape[1]-1 and presentState[rPos]==1):#Right is 1 and below is 0
			if(bPos[0]>presentState.shape[0]-1):  #*11110
				state=rPos                        #xxxxxx
				while(presentState[state]==1):
					state=right(state)
				return state,1	

			if(presentState[bPos]==0):
				if(presentState[brPos]==0):       #*1                                       
					return brPos,0                #00
				else:                             #*1
					return bPos,3                 #01
			
		if(aPos[0]>0 and presentState[aPos]==1):
			if(rPos[1]>presentState.shape[1]-1):  #0x
				state=aPos                        #1x
				while(presentState[state]==1):    #1x
					state=above(state)            #*x
				return state,2	

			if(presentState[rPos]==0):
				if(presentState[arPos]==0):       #10
					return arPos,1                #*0
				else:                             #11
					return rPos,0                 #*0
			
		if(lPos[1]>0 and presentState[lPos]==1):
			if(aPos[0]<0):                         #xxxxxx
				state=lPos                         #01111*
				while(presentState[state]==1):
					state=left(state)
				return state,3
	
			if(presentState[aPos]==0):
				if(presentState[alPos]==0):       #00
					return alPos,2                #1*
				else:                             #10
					return aPos,1                 #1*

		if(bPos[0]<presentState.shape[0]-1 and presentState[bPos]==1):
			if(lPos[1]<0):                         #x*
				state=bPos                         #x1
				while(presentState[state]==1):     #x1
					state=below(state)             #x0
				return state,0
		
			if(presentState[lPos]==0):
				if(presentState[blPos]==0):       #0*
					return blPos,3                #01
				else:                             #0*
					return lPos,2                 #11



state=np.zeros((5,5))
state[2,2]=1
state[2,3]=1
print(findNext(state,(-1,-1)))
