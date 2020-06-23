import time
import serial
import json

ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

ser.flush()
   
splitData=[]
while 1:
    if ser.in_waiting > 0:
        data=ser.readline().decode()
        

        data=data.replace('\r','')
        data=data.replace('\n','')
        splitData=data.split(",")
        print("sys " +splitData[0])
        print("dia " +splitData[1])
        print("pulse " +splitData[2])
        with open("data1.json", "r") as a_file:
            json_object = json.load(a_file)
            
        json_object["sys"]= splitData[0]
        json_object["dia"]=splitData[1]
        json_object["pulse"]=splitData[2]
        
        print(data)
    
        with open("data1.json", "w") as a_file:
            json.dump(json_object, a_file)

        print(json_object)

        
        
