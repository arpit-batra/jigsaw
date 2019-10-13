import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import random 
def plotProgress(finalImage,name):
	# print(finalImage.shape)
	# for i in range(finalImage.shape[0]):
	# 	for j in range(finalImage.shape[1]):
	# 		print(finalImage[i][j].shape)
	img = np.zeros((finalImage.shape[0]*finalImage.shape[2], finalImage.shape[1]*finalImage.shape[3], finalImage.shape[4]))
	idx = 0
	# for i in range(img.shape[0]):
	# 	for j in range(img.shape[1]):
	# 		img[i][j] = finalImage[i*28 + ]
	idy = 0
	for i in range(finalImage.shape[0]):
		# idx=0
		for j in range(finalImage.shape[1]):
			# idy=0
			for k in range(finalImage.shape[2]):
				# idx+=1
				for l in range(finalImage.shape[3]):
					# idy+=1
					# print(str(i*28 + k))
					# print(str(i*28 + k))

					# print(str(j*28 + l) + " - " + str(idy))

					img[i*28 + k][j*28 + l] = finalImage[i][j][k][l]
					# print(finalImage[i][j][k][l])
					# print(img[idx])
	# for i in range(finalImage.shape[0]):
		# for j in range(finalImage.shape[1]):
	# plt.imshow(img)
	cv.imwrite(str(name),img)
	# plt.savefig(name)

a=np.load("pieces.npy")
plotProgress(a,'itsTrue.jpg')