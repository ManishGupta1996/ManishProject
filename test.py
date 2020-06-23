import max30102
import hrcalc
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

spo2Value=[]
value=[]
m = max30102.MAX30102()

for i in range(30): # try 20 times
    red, ir = m.read_sequential() # if nothing is passed, this reads 100 values
    reading = hrcalc.calc_hr_and_spo2(ir, red)
    spo2Value=reading
    if spo2Value[3] == True:
        value.append(spo2Value[2])
##      print(spo2Value[2])
    print(reading)


print(value)
m.shutdown()
print ("\nZ-score for arr1 : \n",abs(stats.zscore(value)))
zValue=abs(stats.zscore(value))
i=[]
temp=[]

for i in range(len(value)):
    if zValue[i] < 2:
        temp.append(value[i])
        

print(temp)
print('mean', np.mean(temp))

i=range(len(temp))
print(i)


plt.plot(i,temp)
plt.xlabel('x - axis')
plt.ylabel('SPO2 level')
plt.title('OxyginLevel')
plt.show()
