import max30102
import hrcalc
import matplotlib.pyplot as plt 


##m = max30102.MAX30102() # sensor initialization
##red, ir = m.read_sequential(200) # get LEDs readings
##print(ir)
##print(red)

##value=hrcalc.calc_hr_and_spo2(ir[20:200], red[20:200])
##print(value)
##print(ir[:300])
##print(red[:300])
##print(len(red[:300]))
##print(len(ir[:300]))

ir2 = []

with open("ir.log", "r") as f:
    for line in f:
        ir2.append(int(line))

print(len(ir2))

red2 = []

with open("red.log", "r") as f:
    for line in f:
        red2.append(int(line))
print(len(red2))

##value=hrcalc.calc_hr_and_spo2(ir2[25:125], red2[25:125])

spo2Value=[]
value=[]
#print(type(num))
####num=value
##print(value)
##print(num[2:4])
for i in range(37):
    #print(i)
    reading=hrcalc.calc_hr_and_spo2(ir2[25*i:25*i+100], red2[25*i:25*i+100])
    spo2Value=reading
    if spo2Value[3] == True:
        value.append(spo2Value[2])
##      print(spo2Value[2])
    print(reading)

print(value)
i=[]
i=range(len(value))
print(i)


plt.plot(i,value)
plt.xlabel('x - axis')
plt.ylabel('Oxigen level')
plt.title('Spo2 Graph')
plt.show()
    



##m.shutdown()
