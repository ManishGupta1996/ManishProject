import max30102
import hrcalc
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import paramiko
import json 
import sys

spo2Value=[]
value=[]
hr=[]
m = max30102.MAX30102()

for i in range(10): # try 20 times
    red, ir = m.read_sequential() # if nothing is passed, this reads 100 values
    reading = hrcalc.calc_hr_and_spo2(ir, red)
    spo2Value=reading
    if spo2Value[3] == True:
        value.append(spo2Value[2])
##      print(spo2Value[2])

    if spo2Value[1] == True:
        hr.append(spo2Value[0])

    print(reading)
    

print("Heart Rate :",hr)
print("Spo2 level:", value)
m.shutdown()
print ("\nZ-score for arr1 : \n",abs(stats.zscore(value)))
zValue=abs(stats.zscore(value))
i=[]
temp=[]

for i in range(len(value)):
    if zValue[i] < 2:
        temp.append(value[i])
        

print(temp)
oxygenMean = np.mean(temp)
print('mean', oxygenMean)

##i=range(len(temp))
##print(i)
##
##
##plt.plot(i,temp)
##plt.xlabel('x - axis')
##plt.ylabel('SPO2 level')
##plt.title('OxyginLevel')
##plt.show()

  
# Data to be store in json file

dictionary ={ 
    "heartRate" : hr, 
    "oxygen" : temp,
    "oxyMean" : oxygenMean,

}
  
# Serializing json  
json_object = json.dumps(dictionary, indent = 2) 
print(dictionary)

storeJsonName = sys.argv[1]
 
# Writing to sample.json 
with open(storeJsonName, "w") as outfile: 
    outfile.write(json_object)

sendLocationServer = '/home/harekrishna/PycharmProjects/django/medicalProject/' + storeJsonName

ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.24.109.38',username='harekrishna', password='m')
sftp_client = ssh.open_sftp()
# sftp_client.get('/home/pi/my_file.txt','my_file.txt')   # file from server to local download
ok=sftp_client.put(storeJsonName,sendLocationServer)   # file from loacl to server send.
print(ok)
sftp_client.close()
ssh.close()

