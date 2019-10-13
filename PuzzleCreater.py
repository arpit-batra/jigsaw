import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import random 
from testing import testing
pieceSize=28


# A function to generate a random permutation of arr[] 
def randomize (arr, length, breadth): 
    # Start from the last element and swap one by one. We don't 
    # need to run for the first element that's why i > 0 
	
	print(length)
	print(breadth)
	for i in range(length):
		for j in range(breadth):
			k=random.randint(0,length-1)
			l=random.randint(0,breadth-1)
			temp=arr[i][j]
			arr[i][j]=arr[k][l]
			arr[k][l]=temp
# print("randomizing")
	return arr 


#Reading Image
completeImage=cv.imread('data/17.jpg')
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
testing(piece)
piece=randomize(piece,int(completeImage.shape[0]/pieceSize),int(completeImage.shape[1]/pieceSize))
testing(piece)
# np.save("pieces.npy",piece) 