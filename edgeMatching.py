import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math
from plotPieces import plotProgress
from findingOrder import findNext
import sys


pieceSize=28

#Reading the jumbled image
unsolvedImage=np.load("pieces.npy")

noHorizontalPatches=unsolvedImage.shape[0]
noVerticalPatches=unsolvedImage.shape[1]

print(noVerticalPatches)    #27
print(noHorizontalPatches)  #20

###############################
#To get cost between two edges#
###############################



#Euclidean distance between two 3dimensional points
def EucDistance(point1,point2):
	result=0
	for i in range(3):
		result+=(point1[i]-point2[i])**2
	return math.sqrt(result)

#To get cost/distance between two edges
def egdeCost(edge1,edge2):
	result=0
	for i in range(pieceSize):
		result+=EucDistance(edge1[i],edge2[i])
	return result



#########################
#To get edges of a patch#
#########################


#To get left Edge of a patch
def leftEdge(patch):
	result=np.zeros((pieceSize,3))
	for i in range(pieceSize):
		result[i]=patch[i][0]
	return result

#To get top Edge of a patch
def topEdge(patch):
	result=np.zeros((pieceSize,3))
	for i in range(pieceSize):
		result[i]=patch[0][i]
	return result

#To get right Edge of a patch
def rightEdge(patch):
	result=np.zeros((pieceSize,3))
	for i in range(pieceSize):
		result[i]=patch[i][pieceSize-1]
	return result

#To get bottom Edge of a patch
def bottomEdge(patch):
	result=np.zeros((pieceSize,3))
	for i in range(pieceSize):
		result[i]=patch[pieceSize-1][i]
	return result

def printFull(matrix):
	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			print(int(matrix[i][j]),end=" ")
		print("")

updatedImage=np.zeros((unsolvedImage.shape))
print(updatedImage.shape)
#(20, 27, 28, 28, 3)


#SomeTesting
########################################################
# test=unsolvedImage[0][0]
# for i in range(test.shape[0]):
# 	for j in range(test.shape[1]):
# 		print(test[i][j])
# 	print("\n")
# print(test.shape)
# print("leftEdge")
# print(leftEdge(test))
# print("rightEdge")
# print(rightEdge(test))
# print("topEdge")
# print(topEdge(test))
# print("bottomEdge")
# print(bottomEdge(test))
# print(egdeCost(leftEdge(test),leftEdge(test)))

# print(egdeCost(leftEdge(test),rightEdge(test)))
#########################################################



#This keeps info of where patches are added in the update image
#1 means present

updateInfo=np.zeros((noHorizontalPatches,noVerticalPatches))

#This keeps the info of which patches are taken from the previous image

patchesTaken=np.zeros((noHorizontalPatches,noVerticalPatches))


##########################################
#Placing first random patch in the centre#
##########################################
updatedImage[int(updatedImage.shape[0]/2)][int(updatedImage.shape[1]/2)]=unsolvedImage[0][0]
updateInfo[int(updatedImage.shape[0]/2)][int(updatedImage.shape[1]/2)]=1
patchesTaken[0][0]=1



# Direction from findNext
# 0-Above
# 1-Left
# 2-Below
# 3-Right


#currentPatch and currentPatch2 are the variables with which we are going to match our edge costs

counter=0
nextPosition=-1,-1
summ=0
while(1):
	temp=findNext(updateInfo,nextPosition)
	print(temp)
	nextPosition=temp[0]
#if this patch is totally surrounded
	leftPatchPos=nextPosition[0],nextPosition[1]-1
	rightPatchPos=nextPosition[0],nextPosition[1]+1
	abovePatchPos=nextPosition[0]-1,nextPosition[1]
	belowPatchPos=nextPosition[0]+1,nextPosition[1]
	
	suitablePatchPosition=0,0	
	minEdgeCost=sys.maxsize
	if(updateInfo[leftPatchPos]==1 and updateInfo[rightPatchPos]==1 and updateInfo[abovePatchPos]==1 and updateInfo[belowPatchPos]==1):
		
		leftPatch=updatedImage[leftPatchPos]
		rightPatch=updatedImage[rightPatchPos]
		abovePatch=updatedImage[abovePatchPos]
		belowPatch=updatedImage[belowPatchPos]

		for i in range(noHorizontalPatches):
			for j in range(noVerticalPatches):
				if(patchesTaken[i][j]==0):
					edgeCost = egdeCost(rightEdge(leftPatch),leftEdge(unsolvedImage[i][j]))+egdeCost(leftEdge(rightPatch),rightEdge(unsolvedImage[i][j]))+egdeCost(topEdge(belowPatch),bottomEdge(unsolvedImage[i][j]))+egdeCost(bottomEdge(abovePatch),topEdge(unsolvedImage[i][j]))
					if(edgeCost<minEdgeCost):
						suitablePatchPosition=i,j
						minEdgeCost=edgeCost
		patchesTaken[suitablePatchPosition]=1
		updateInfo[nextPosition]=1
		updatedImage[nextPosition]=unsolvedImage[suitablePatchPosition]
#if not
	direction=temp[1]
	if(direction==0):
		currentPatchPos=nextPosition[0]-1,nextPosition[1]   #Current patch above nextPosition
	elif(direction==1):
		currentPatchPos=nextPosition[0],nextPosition[1]-1   #Current patch left of nextPosition
	elif(direction==2):
		currentPatchPos=nextPosition[0]+1,nextPosition[1]   #Current patch below nextPosition
	else:
		currentPatchPos=nextPosition[0],nextPosition[1]+1   #Current patch right of nextPosition

	currentPatch=updatedImage[currentPatchPos]
	#Finding the best match
	suitablePatchPosition=0,0
	minEdgeCost=sys.maxsize
	if(direction==0):
		for i in range(noHorizontalPatches):       #Iterating all patches   
			for j in range(noVerticalPatches):
				if(patchesTaken[i][j]==0):           #Considering only those which are still not part of our updatedImage 
					edgecost1 = egdeCost(bottomEdge(currentPatch),topEdge(unsolvedImage[i][j]))
					currentPatch2Pos = currentPatchPos[0]+1, currentPatchPos[1]+1
					if(currentPatch2Pos[0] < unsolvedImage.shape[0] and currentPatch2Pos[1] < unsolvedImage.shape[1] and updateInfo[currentPatch2Pos]==1):
						currentPatch2 = updatedImage[currentPatch2Pos]
						edgecost2 = egdeCost(leftEdge(currentPatch2),rightEdge(unsolvedImage[i][j]))
					else:
						edgecost2 = 0
					if(edgecost1 + edgecost2 < minEdgeCost):
						suitablePatchPosition=i,j
						minEdgeCost = edgecost1 + edgecost2
		if(minEdgeCost<1000):
			patchesTaken[suitablePatchPosition]=1
			updateInfo[nextPosition]=1
			updatedImage[nextPosition]=unsolvedImage[suitablePatchPosition]
				

	elif(direction==1):
		for i in range(noHorizontalPatches):       #Iterating all patches   
			for j in range(noVerticalPatches):
				if(patchesTaken[i][j]==0):           #Considering only those which are still not part of our updatedImage 
					edgecost1 = egdeCost(rightEdge(currentPatch),leftEdge(unsolvedImage[i][j]))
					currentPatch2Pos = currentPatchPos[0]-1, currentPatchPos[1]+1
					if(currentPatch2Pos[0] >= 0 and currentPatch2Pos[1] < unsolvedImage.shape[1] and updateInfo[currentPatch2Pos]==1):
						currentPatch2 = updatedImage[currentPatch2Pos]
						edgecost2 = egdeCost(bottomEdge(currentPatch2),topEdge(unsolvedImage[i][j]))
					else:
						edgecost2 = 0
					if(edgecost1 + edgecost2 < minEdgeCost):
						suitablePatchPosition=i,j
						minEdgeCost = edgecost1 + edgecost2
		if(minEdgeCost<1000):
			patchesTaken[suitablePatchPosition]=1
			updateInfo[nextPosition]=1
			updatedImage[nextPosition]=unsolvedImage[suitablePatchPosition]
	


	elif(direction==2):
		for i in range(noHorizontalPatches):       #Iterating all patches   
			for j in range(noVerticalPatches):
				if(patchesTaken[i][j]==0):           #Considering only those which are still not part of our updatedImage 
					edgecost1 = egdeCost(topEdge(currentPatch),bottomEdge(unsolvedImage[i][j]))
					currentPatch2Pos = currentPatchPos[0]-1, currentPatchPos[1]-1
					
					if(currentPatch2Pos[0] >= 0 and currentPatch2Pos[1] >= 0  and updateInfo[currentPatch2Pos]==1):
						currentPatch2 = updatedImage[currentPatch2Pos]
						edgecost2 = egdeCost(rightEdge(currentPatch2),leftEdge(unsolvedImage[i][j]))
					else:
						edgecost2 = 0
					if(edgecost1 + edgecost2 < minEdgeCost):
						suitablePatchPosition=i,j
						minEdgeCost = edgecost1 + edgecost2
		if(minEdgeCost<1000):
			patchesTaken[suitablePatchPosition]=1
			updateInfo[nextPosition]=1
			updatedImage[nextPosition]=unsolvedImage[suitablePatchPosition]
	


	else:
		for i in range(noHorizontalPatches):       #Iterating all patches   
			for j in range(noVerticalPatches):
				if(patchesTaken[i][j]==0):           #Considering only those which are still not part of our updatedImage 
					edgecost1 = egdeCost(leftEdge(currentPatch),rightEdge(unsolvedImage[i][j]))
					currentPatch2Pos = currentPatchPos[0]+1, currentPatchPos[1]-1
					if(currentPatch2Pos[0] < unsolvedImage.shape[0] and currentPatch2Pos[1] >= 0  and updateInfo[currentPatch2Pos]==1):
						currentPatch2 = updatedImage[currentPatch2Pos]
						edgecost2 = egdeCost(topEdge(currentPatch2),bottomEdge(unsolvedImage[i][j]))
					else:
						edgecost2 = 0
					if(edgecost1 + edgecost2 < minEdgeCost):
						suitablePatchPosition=i,j
						minEdgeCost = edgecost1 + edgecost2
		if(minEdgeCost<1000):
			patchesTaken[suitablePatchPosition]=1
			updateInfo[nextPosition]=1
			updatedImage[nextPosition]=unsolvedImage[suitablePatchPosition]
	summ+=(minEdgeCost/1000)
	# plotProgress(unsolvedImage,"check/"+str(counter)+".jpg")
	# print(suitablePatchPosition)
	print(minEdgeCost)
	print(summ)
	#Plotting updated image
	printFull(updateInfo )
	plotProgress(updatedImage,"Results1/"+str(counter)+".jpg")
	counter+=1