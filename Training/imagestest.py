# # Grey scale images

# # import cv2
# # import os

# # os.chdir("/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/DataD")
# # te = os.listdir()
# # j = 535
# # for i in te:
# #     img = cv2.imread(i,0)
# #     resize = cv2.resize(img,(500,500))
# #     file = f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/images/{j}.png"
# #     print(j)
# #     j = j+1
# #     cv2.imwrite(file, resize)
    
# #     print(i)




# # img =  cv2.imread('images/20230104_155623.jpg',0)
# # resize = cv2.resize(img,(500,500))
# # cv2.imshow("img",resize )
# # cv2.waitKey(0)
# # cv2.destroyWindow


# '''

# # video on grey scale images

# import cv2

# cap = cv2.VideoCapture(2)

# while (True):
#     _, frame = cap.read()
#     Resize = cv2.resize(frame,(500,500))
#     frames = cv2.cvtColor(Resize, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("Live", frames)
#     # exiting the loop
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break
    
# '''

# """

# # black and white windows on videos

# import cv2 as cv
# import numpy as np

# def nothing(x):pass

# cap = cv.VideoCapture(2)
# cv.namedWindow('videoUI', cv.WINDOW_NORMAL)
# cv.createTrackbar('T','videoUI',0,255,nothing)

# while(True):
#     ret, frame = cap.read()
#     vid_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     thresh = cv.getTrackbarPos('T','videoUI');
#     vid_bw = cv.threshold(vid_gray, thresh, 255, cv.THRESH_BINARY)[1]

#     cv.imshow('videoUI',cv.flip(vid_bw,1))

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()
# """



# # DataAgmentation scale images

import cv2
import os

ls = "/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Items/ItemC"
os.chdir("/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Items/ItemC")

img_file = os.listdir('/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Items/ItemC')
print(img_file)
m = len(img_file)

print(m)

img = os.listdir("/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Items/images/")
n = len(img)
print(n)


for i in img_file:
    Data = cv2.imread(i)
    Resize = cv2.resize(Data,(500,500))
    frames = cv2.cvtColor(Resize, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Items/images/{n}.jpg",frames)
    print(n)
    n=n+1
    image = cv2.flip(frames, 0)
    cv2.imwrite(f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Agmented/{n}.jpg",image)
    print(n)
    n=n+1
    
    h,w = frames.shape[:2]
    cr = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(cr, 30, 1)
    rotate = cv2.warpAffine(frames,M,(w,h))
    cv2.imwrite(f"datasets/Gray/Agmented/{n}.jpg",rotate)
    print(n)
    n=n+1
    
# #     h,w = frames.shape[:2]
# #     cr = (w / 2, h / 2)
# #     M = cv2.getRotationMatrix2D(cr, 270, 1)
# #     rotate = cv2.warpAffine(frames,M,(w,h))
# #     cv2.imwrite(f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Agmented/{n}.jpg",rotate)
# #     print(n)
# #     n=n+1
#     # 
#     # M = cv2.getRotationMatrix2D(cr, 90, 1)
#     # rotate = cv2.warpAffine(data,M,(w,h))
#     # ressiz = cv2.resize(rotate,(500,500))
#     # cv2.imwrite(f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Agmented/{n}.jpg",ressiz)
#     # n=n+1
#     # print(n)
#     # M = cv2.getRotationMatrix2D(cr, 160, 1)
#     # rotate = cv2.warpAffine(data,M,(w,h))
#     # ressiz = cv2.resize(rotate,(500,500))
#     # cv2.imwrite(f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Agmented/{n}.jpg",ressiz)
#     # n=n+1
#     # print(n)
# #     M = cv2.getRotationMatrix2D(cr, 190, 1)
# #     rotate = cv2.warpAffine(data,M,(w,h))
# #     ressiz = cv2.resize(rotate,(500,500))
# #     cv2.imwrite(f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Agmented/{n}.jpg",ressiz)
# #     n=n+1
# #     M = cv2.getRotationMatrix2D(cr, 230, 1)
# #     rotate = cv2.warpAffine(data,M,(w,h))
# #     ressiz = cv2.resize(rotate,(500,500))
# #     cv2.imwrite(f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Agmented/{n}.jpg",ressiz)
# #     n=n+1
# #     M = cv2.getRotationMatrix2D(cr, 270, 1)
# #     rotate = cv2.warpAffine(data,M,(w,h))
# #     ressiz = cv2.resize(rotate,(500,500))
# #     cv2.imwrite(f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Agmented/{n}.jpg",ressiz)
# #     n=n+1
# #     M = cv2.getRotationMatrix2D(cr, 330, 1)
# #     rotate = cv2.warpAffine(data,M,(w,h))
# #     ressiz = cv2.resize(rotate,(500,500))
# #     cv2.imwrite(f"/home/usamah/Documents/Office_project/Car_Parts_detection/Training/datasets/Gray/Agmented/{n}.jpg",ressiz)
# #     n=n+1