import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import random 
from testing import testing
pieceSize=28


# A function to generate a random permutation of arr[] 
def randomize (arr): 
    # Start from the last element and swap one by one. We don't 
    # need to run for the first element that's why i > 0 
	length=arr.shape[0]
	breadth=arr.shape[1]
	TempAns=np.zeros(arr.shape)
	occupied=np.zeros((length,breadth))

	print(length)
	print(breadth)
	print(TempAns)
	
	for i in range(length):
		for j in range(breadth):
			k=random.randint(0,length-1)
			l=random.randint(0,breadth-1)
			temp=TempAns[i][j]
			TempAns[i][j]=TempAns[k][l]
			TempAns[k][l]=temp
# print("randomizing")
	return TempAns 


#Reading Image
completeImage=cv.imread('data/7.jpg')
# cv.imshow("img", completeImage)
# print(completeImage.shape)
# cv.waitKey(0)

# #Swapping R and B because matplotlib plots that way
# for i in range(completeImage.shape[0]):
# 	for j in range(completeImage.shape[1]):
# 		temp=completeImage[i][j][0]
# 		completeImage[i][j][0]=completeImage[i][j][1]
# 		completeImage[i][j][1]=temp
# print(completeImage)
# print(completeImage.size)
# print(completeImage.shape)

# plt.imshow(completeImage)
# plt.savefig("data/completeImage")
#Plotting
# plt.imshow(completeImage)
# plt.show()

#Initializing Piece
piece=np.zeros((int(completeImage.shape[0]/pieceSize),int(completeImage.shape[1]/pieceSize),pieceSize,pieceSize,3))
print(piece.shape)
#Saving pieces in piece folder

print(int(completeImage.shape[0]/pieceSize))
print(int(completeImage.shape[1]/pieceSize))

for i in range (int(completeImage.shape[0]/pieceSize)):
	for j in range(int(completeImage.shape[1]/pieceSize)):
		for k in range(pieceSize):
			for l in range(pieceSize):
				for m in range(3):
				# print(completeImage[int((i*pieceSize)+k)][int((j*pieceSize)+l)])
					piece[i][j][k][l][m]=completeImage[int((i*pieceSize)+k)][int((j*pieceSize)+l)][m]
					# print("hello")
		# print(piece)
		# plt.imshow(piece)
		# plt.savefig("pieces/"+str(i)+" "+str(j)+".jpg")
# testing(piece)

length=piece.shape[0]
breadth=piece.shape[1]
print(length)
print(breadth)
reference=np.zeros((length,breadth))
counter=0
for i in range(length):
	for j in range(breadth):
		reference[i][j]=counter
		counter+=1

print(reference)
print("")
for i in range(length):
	for j in range(breadth):
		k=random.randint(0,length-1)
		l=random.randint(0,breadth-1)
		reference[i][j],reference[k][l]=reference[k][l],reference[i][j]
print(reference)

TempAns=np.zeros(piece.shape)

for i in range(length):
	for j in range(breadth):
		print(int(reference[i][j]/breadth))
		print(int(reference[i][j]%breadth))
		TempAns[i][j]=piece[int(reference[i][j]/breadth)][int(reference[i][j]%breadth)]

# testing(TempAns)
np.save("pieces.npy",TempAns) 