import cv2
win_size=(48,96)
block_size=(16,16)
block_stride=(8,8)
cell_size=(8,8)
num_bins=9
hog=cv2.HOGDescriptor(win_size,block_size,block_stride,cell_size,num_bins)

print(hog)