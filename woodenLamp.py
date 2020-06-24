import cv2
import numpy as np

###### Read any images ############
# img =cv2.imread("Resources/manisPhoto.jpg")
# cv2.imshow("manishPhoto", img)
# cv2.waitKey(2000)


######### read any live video#########
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1)  & 0xFF ==ord('q'):
#         break


####### Some function ##################

# img = cv2.imread("Resources/RiyaPhoto1.jpeg")
# img = cv2.resize(img,(300,300))
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# imgBlur= cv2.GaussianBlur(imgGray,(7,7),1)
# imgCanny = cv2.Canny(img, 15,200)
# #
# #
# cv2.imshow("Gray image", imgGray)
# cv2.imshow("blur image",imgBlur)
# cv2.imshow("Canny image",imgCanny)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
############ Resize and crope image ######################
# img=cv2.imread("Resources/photo1.jpg")
# print(img.shape)
# imgResize = cv2.resize(img,(150,150))
# print(imgResize.shape)
# imgCrope = img[0:200,100:150]
# cv2.imshow("img",img)
# cv2.imshow("imgResize",imgResize)
# cv2.imshow("Crope image",imgCrope)
# cv2.imwrite("Resources/resizeImage.jpg",imgResize)   ## to save resize image into the folder
# cv2.waitKey(0)


################## Shape and text ##############

# img = np.zeros((512,512,3),np.uint8)
# img1=cv2.imread("Resources/photo1.jpg")
# # img[:]=0,0,255
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(10,200,0),2)
# cv2.rectangle(img, (0,0),(250,350),(0,0,255),2)
# cv2.circle(img,(400,50),30,(255,255,0),5)
# cv2.putText(img1,"open cv",(50,180),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
# cv2.putText(img,"open cv",(300,180),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
# cv2.imshow("text",img1)
# cv2.imshow("image", img)
# cv2.waitKey(0)



###################### joine image ###################

# img=cv2.imread('Resources/photo1.jpg')
# imgHor=np.hstack((img,img))
# imgVer = np.vstack((img,img))
# r=cv2.imread('Resources/did.jpeg')
# print(r.shape)
# imgResize = cv2.resize(r,(300,300))
# rGray=cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
# rHor1=np.hstack((imgResize,imgResize))
# rHor2=np.hstack((imgResize,imgResize))
# rVer=np.vstack((rHor1,rHor2))
# rHor1=np.hstack((rGray,rGray))
# rHor2=np.hstack((rGray,rGray))
# rVer=np.vstack((rHor1,rHor2))
# cv2.imshow("horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
# cv2.imshow("Riya",r)
# cv2.imshow("RiyaResize1",rHor1)
# cv2.imshow("RiyaResize2",rHor2)
# cv2.imshow("result",rVer)
# # cv2.imshow('gray',rGray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



################################### file transfer local to server and vice versa ########################
import paramiko
ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.24.110.107',username='pi', password='123')
sftp_client = ssh.open_sftp()
# sftp_client.get('/home/pi/my_file.txt','my_file.txt')   # file from server to local download
sftp_client.put("woodenLamp.py",'/home/pi/Documents/Anuj/woodenLamp.py')   # file from loacl to server send.
sftp_client.close()
ssh.close()

#################### Face dedection #####################

# faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
# img = cv2.imread("Resources/lena.png")
# # img = cv2.resize(img,(150,150))
# grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# facse= faceCascade.detectMultiScale(grayImg, 1.1,4)
# for x,y,w,h in facse:
#     img = cv2.resize(img,(x,y),(x+w,y+h),(0,255,0),3)
#
# resized = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))
# cv2.imshow("gray",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
#
# faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
# img = cv2.imread('Resources/lena.png')
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)
#
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#
#
# cv2.imshow("Result", img)
# cv2.waitKey(0)



################## Capture image and save it ###########################

# video= cv2.VideoCapture(0)
# result =True
# while(result):
#     ret,frame=video.read()
#     cv2.imwrite("NewPicture.jpg",frame)
#     result=False
#
# video.release()
# cv2.destroyAllWindows()









