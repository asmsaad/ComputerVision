import cv2 as cv
import numpy as np


#todo Read an image
# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)
# cv.destroyAllWindows()



#todo Read a video
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)    
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break


#todo Resize frame
#? Use for Images , Videos and Live video
# def resizeFrame(frame, scale=0.75):
#     height,width = frame.shape[:2]
#     height,width = int(height*scale), int(width*scale)
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)    
#     cv.imshow('Video2', resizeFrame(frame, scale=0.25))    
    
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
    
    
#todo Change live video dimensions
#? Only Works for live Video
# capture = cv.VideoCapture(0)
# def changeRes(width, height):
#     capture.set(3, width)
#     capture.set(4, height)



#todo Draw Shapes/ Write Text
# blank_img = np.zeros((500,500), dtype='uint8')
# cv.imshow('Blank Image', blank_img)
# cv.waitKey(0)

# #                         Color Chanel
# #                             v
# blank_img = np.zeros((500,500,3), dtype='uint8')
# #              B   G   R
# blank_img[:] = 0, 255, 0
# cv.imshow('Blank Image', blank_img)
# cv.waitKey(0)

# blank_img = np.zeros((500,500,3), dtype='uint8')
# blank_img[200:300, 300:400] = 0, 255, 0
# cv.imshow('Blank Image', blank_img)
# cv.waitKey(0)

#? Draw a rectangel
# blank_img = np.zeros((500,500,3), dtype='uint8')
# # cv.rectangle(blank_img, (100,100), (300,300), (0,255,0),thickness=1)
# # cv.rectangle(blank_img, (100,100), (300,300), (0,255,0),thickness=cv.FILLED)   # Used for filling
# # cv.rectangle(blank_img, (100,100), (300,300), (0,255,0),thickness=-1)          # Used for filling
# cv.rectangle(blank_img, (0,0), (blank_img.shape[1]//2, blank_img.shape[0]//2), (0,255,0),thickness=-1)
# cv.imshow('Blank Image', blank_img)
# cv.waitKey(0)

#? Draw a Circle
# blank_img = np.zeros((500,500,3), dtype='uint8')
# cv.circle(blank_img, (blank_img.shape[1]//2, blank_img.shape[0]//2), 50, (0,0,255), thickness=1)                                #? Circle
# cv.line(blank_img, (0, blank_img.shape[1]//2), (blank_img.shape[0], blank_img.shape[1]//2), (0,255,0), thickness=1 )            #? Line
# cv.putText(blank_img, 'Saad', (blank_img.shape[1]//2, blank_img.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)   #? Text
# cv.imshow('Blank Image', blank_img  )
# cv.waitKey(0)


#todo Essential Functions 
# img  = cv.imread("./Resources/Photos/lady.jpg")

# # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)             #? Grayscal Image
# # img = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)  #? Blur Image
# # img = cv.Canny(img, 400, 200, cv.BORDER_DEFAULT)      #? Edge  Cascade

# #? Dilating Image
# # img = cv.Canny(img, 150, 150, cv.BORDER_DEFAULT)
# # img = cv.dilate(img, (2,2), iterations=1)    
# # img = cv.erode(img, (2,2), iterations=1)    

# # img = cv.resize(img, (200,200), interpolation=cv.INTER_CUBIC)     #? Resizing
# # img = img[100:300 , 300:400]                                        #? Crope

# cv.imshow("Image", img)
# cv.waitKey(0)



#todo  Image Transformations
img = cv.imread("./Resources/Photos/lady.jpg")









