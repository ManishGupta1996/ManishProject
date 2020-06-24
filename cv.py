import cv2
import paramiko
import numpy as np
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin (connect to push button) and set initial value to be pulled low (off)
GPIO.setup(7,GPIO.OUT)
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture(0) 

jpg=".jpg"   
i=0
# Check if camera opened successfully 
if (cap.isOpened()== False):  
  print("Error opening video  file") 
   
# Read until video is completed 
while(cap.isOpened()): 
      
  # Capture frame-by-frame 
  ret, frame = cap.read() 
  if ret == True: 
   
    # Display the resulting frame 
    cv2.imshow('Frame', frame)
    if GPIO.input(10) == GPIO.HIGH:
      print("image click")
      GPIO.output(7,True)
      i=i+1
      picture="picture"+str(i)+jpg
      cv2.imwrite(picture,frame)
      ssh= paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(hostname='172.24.109.38',username='harekrishna', password='m')
      sftp_client = ssh.open_sftp()
      # sftp_client.get('/home/pi/my_file.txt','my_file.txt')   # file from server to local download
      sendImage='/home/harekrishna/woodenLamp/' +picture
      sftp_client.put(picture,sendImage)   # file from loacl to server send.
      sftp_client.close()
      ssh.close()
      time.sleep(1)

    GPIO.output(7,False)

   
    # Press Q on keyboard to  exit 
    if cv2.waitKey(25) & 0xFF == ord('q'): 
      break



   
  # Break the loop 
  else:  
    break
   
# When everything done, release  
# the video capture object 
cap.release() 
GPIO.cleanup()  
# Closes all the frames 
cv2.destroyAllWindows()
